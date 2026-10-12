import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Job Market Skills Analysis", page_icon="📊", layout="wide")

st.title("📊 Job Market Skills Analysis")
st.write("Analyze in-demand skills, job openings, and salary trends using Pandas, NumPy, and Matplotlib.")
st.caption("Demo project: the included dataset is illustrative sample data, not live job-market statistics.")

@st.cache_data
def load_data():
    return pd.read_csv("job_market_data.csv")

df = load_data()

st.sidebar.header("Filters")
skills = st.sidebar.multiselect("Choose skills", options=df["Skill"].unique(), default=list(df["Skill"].unique()))
filtered = df[df["Skill"].isin(skills)].copy()

if filtered.empty:
    st.warning("Select at least one skill from the sidebar.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Total sample job openings", f"{int(np.sum(filtered['Job_Openings'])):,}")
c2.metric("Average openings per skill", f"{np.mean(filtered['Job_Openings']):,.1f}")
c3.metric("Average estimated salary", f"₹{np.mean(filtered['Avg_Salary_LPA']):.1f} LPA")

st.subheader("Dataset")
st.dataframe(filtered, use_container_width=True, hide_index=True)

top = filtered.sort_values("Job_Openings", ascending=False).iloc[0]
st.info(f"Most demanded skill in the selected sample: **{top['Skill']}** ({int(top['Job_Openings'])} sample openings).")

st.subheader("Job Openings by Skill")
fig1, ax1 = plt.subplots(figsize=(10, 4.5))
ordered = filtered.sort_values("Job_Openings", ascending=False)
ax1.bar(ordered["Skill"], ordered["Job_Openings"])
ax1.set_xlabel("Technical skill")
ax1.set_ylabel("Sample job openings")
ax1.set_title("Job Openings by Technical Skill")
ax1.tick_params(axis="x", rotation=30)
fig1.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

left, right = st.columns(2)
with left:
    st.subheader("Share of Sample Openings")
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.pie(filtered["Job_Openings"], labels=filtered["Skill"], autopct="%1.1f%%", startangle=90)
    ax2.set_title("Job Opening Distribution")
    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

with right:
    st.subheader("Estimated Average Salary by Skill")
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    salary_order = filtered.sort_values("Avg_Salary_LPA", ascending=False)
    ax3.bar(salary_order["Skill"], salary_order["Avg_Salary_LPA"])
    ax3.set_xlabel("Technical skill")
    ax3.set_ylabel("Estimated salary (LPA)")
    ax3.set_title("Estimated Average Salary by Skill")
    ax3.tick_params(axis="x", rotation=45)
    fig3.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)

st.subheader("Summary")
st.write(f"- Highest sample openings: **{top['Skill']}**.")
salary_top = filtered.loc[filtered["Avg_Salary_LPA"].idxmax()]
st.write(f"- Highest estimated average salary in this sample: **{salary_top['Skill']}** (₹{salary_top['Avg_Salary_LPA']:.1f} LPA).")
st.write("- Use these charts to compare skills and plan further learning. Real-world results depend on the source, location, and date of job listings.")

st.download_button(
    "Download filtered data as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="filtered_job_market_data.csv",
    mime="text/csv"
)
