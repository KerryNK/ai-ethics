import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from aif360.datasets import StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric

def load_compas_data(filepath):
    df = pd.read_csv(filepath)
    df = df[
        (df["days_b_screening_arrest"] <= 30) &
        (df["days_b_screening_arrest"] >= -30) &
        (df["is_recid"] != -1) &
        (df["c_charge_degree"] != 'O') &
        (df["score_text"] != 'N/A')
    ].reset_index(drop=True)
    return df

def preprocess_compas_data(df):
    df = df[df['race'].isin(['Caucasian', 'African-American'])]
    race_map = {'Caucasian': 0, 'African-American': 1}
    sex_map = {'Male': 0, 'Female': 1}
    df['race_num'] = df['race'].map(race_map)
    df['sex_num'] = df['sex'].map(sex_map)
    df['label'] = df['two_year_recid']
    df['pred'] = (df['score_text'] == 'High').astype(int)
    return df

def create_aif360_dataset(df):
    return StandardDataset(
        df,
        label_name='label',
        favorable_classes=[0],
        protected_attribute_names=['race_num'],
        privileged_classes=[[0]]
    )

def calculate_bias_metrics(dataset):
    metric = BinaryLabelDatasetMetric(
        dataset,
        privileged_groups=[{'race_num': 0}],
        unprivileged_groups=[{'race_num': 1}]
    )
    return {
        'False Positive Rate (Caucasian)': metric.false_positive_rate(privileged=True),
        'False Positive Rate (African-American)': metric.false_positive_rate(privileged=False),
        'Disparate Impact': metric.disparate_impact(),
        'Average Odds Difference': metric.average_odds_difference()
    }

def plot_false_positive_rates(df):
    results = []
    for race, label in zip([0, 1], ['Caucasian', 'African-American']):
        group = df[df['race_num'] == race]
        fp = ((group['pred'] == 1) & (group['label'] == 0)).sum()
        n_neg = (group['label'] == 0).sum()
        fpr = fp / n_neg if n_neg > 0 else 0
        results.append({'race': label, 'false_positive_rate': fpr})
    plot_df = pd.DataFrame(results)
    sns.barplot(x='race', y='false_positive_rate', data=plot_df, palette='muted')
    plt.title('False Positive Rate by Race')
    plt.ylabel('False Positive Rate')
    plt.xlabel('Race')
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

def plot_risk_score_distribution(df):
    score_map = {'Low': 0, 'Medium': 1, 'High': 2}
    df['score_num'] = df['score_text'].map(score_map)
    race_labels = {0: 'Caucasian', 1: 'African-American'}
    df['race_label'] = df['race_num'].map(race_labels)
    sns.boxplot(x='race_label', y='score_num', data=df, palette='pastel')
    plt.title('Distribution of COMPAS Risk Scores by Race')
    plt.xlabel('Race')
    plt.ylabel('Risk Score (0=Low, 1=Medium, 2=High)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filepath = "compas-scores-two-years.csv"  # Update path accordingly
    df = load_compas_data(filepath)
    df = preprocess_compas_data(df)
    dataset = create_aif360_dataset(df)
    metrics = calculate_bias_metrics(dataset)

    print("Bias Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    plot_false_positive_rates(df)
    plot_risk_score_distribution(df)
