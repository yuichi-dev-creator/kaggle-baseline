def preprocess(df):
    # 安全に動く最小構成
    if "Rainfall_mm" in df.columns and "Previous_Irrigation_mm" in df.columns:
        df["water_balance"] = df["Rainfall_mm"] - df["Previous_Irrigation_mm"]
    return df
