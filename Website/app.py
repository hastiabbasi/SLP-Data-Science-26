import streamlit as st
import pandas as pd
import numpy as np
import base64
import re
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="TensorFlowed | Spaceship Titanic",
    page_icon="T",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --ink: #f8fafc;
    --muted: #cbd5e1;
    --purple: #b8a8ff;
    --cyan: #74e4e7;
    --pink: #f6a8d5;
    --cream: #0f172a;
    --card: transparent;
}
html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
    color: var(--ink);
}
.stApp, .stApp p, .stApp li, .stApp label,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stWidgetLabel"] {
    color: #f8fafc !important;
}
.stCaption, [data-testid="stCaptionContainer"] {
    color: #cbd5e1 !important;
}
.stApp input, .stApp textarea, .stApp select,
.stApp [data-baseweb="select"] * {
    color: #f8fafc !important;
    background-color: #1e293b !important;
}
.stApp [data-testid="stAlert"] {
    background: transparent !important;
    border: 1px solid #64748b !important;
}
.stApp [data-testid="stAlert"] * {
    color: #f8fafc !important;
}
.stApp [data-testid="stDataFrame"] * {
    color: #f8fafc !important;
}
.stApp [data-baseweb="tab-list"] button,
.stApp [data-testid="stRadio"] label,
.stApp [data-testid="stRadio"] p {
    color: #f8fafc !important;
}
.stApp {
    background: var(--cream);
}
h1, h2, h3 {
    font-family: "Space Grotesk", sans-serif !important;
    color: var(--ink);
}
.hero {
    padding: 2.4rem 2.7rem 2.2rem;
    border-radius: 28px;
    background: linear-gradient(120deg, #1b2143 0%, #3c3478 55%, #6f55d9 100%);
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 18px 45px rgba(39,31,92,.20);
}
.hero-content {
    position: relative;
    z-index: 2;
    max-width: 78%;
}
.hero-logo {
    position: absolute;
    right: 2.5rem;
    top: 50%;
    width: 150px;
    height: 150px;
    transform: translateY(-50%);
    animation: logo-spin 24s linear infinite;
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.28));
}
@keyframes logo-spin {
    from { transform: translateY(-50%) rotate(0deg); }
    to { transform: translateY(-50%) rotate(360deg); }
}
.hero h1 {
    color: white !important;
    font-size: 3.1rem;
    margin: 0;
    letter-spacing: -.08rem;
}
.hero p {
    color: rgba(255,255,255,.84);
    font-size: 1.08rem;
    max-width: 700px;
    margin: .6rem 0 0;
}
.badge {
    display: inline-block;
    padding: .35rem .7rem;
    margin-bottom: .7rem;
    border-radius: 999px;
    background: rgba(255,255,255,.15);
    color: #e9e5ff;
    font-size: .8rem;
    font-weight: 700;
    letter-spacing: .08rem;
    text-transform: uppercase;
}
.section-label {
    color: var(--purple);
    font-size: .78rem;
    font-weight: 700;
    letter-spacing: .12rem;
    text-transform: uppercase;
    margin-top: 1.5rem;
}
.metric-card {
    background: transparent;
    border: 1px solid #64748b;
    border-radius: 18px;
    padding: 1.2rem 1.3rem;
    box-shadow: none;
    min-height: 112px;
}
.metric-label {
    color: var(--muted);
    font-size: .84rem;
    font-weight: 600;
}
.metric-value {
    color: var(--ink);
    font-family: "Space Grotesk", sans-serif;
    /* Keep the four Mission Control values on one line. */
    font-size: 1.28rem;
    font-weight: 700;
    letter-spacing: -.035em;
    margin-top: .35rem;
    white-space: nowrap;
}
.metric-note {
    color: var(--purple);
    font-size: .78rem;
    margin-top: .25rem;
}
.story-card {
    background: transparent;
    border: 1px solid #64748b;
    border-left: 5px solid var(--cyan);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    box-shadow: none;
}
.story-card strong { color: #ffffff !important; }
.team-card {
    border: 1px solid #64748b;
    border-radius: 16px;
    padding: 1rem;
    min-height: 240px;
    text-align: center;
    background: transparent;
}
.team-card img {
    width: 120px !important;
    height: 120px !important;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid #74e4e7;
    margin: 0 auto .75rem auto;
}
.team-initials {
    width: 120px;
    height: 120px;
    margin: 0 auto .75rem auto;
    border-radius: 50%;
    border: 3px solid #74e4e7;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #1e293b;
    color: #f8fafc;
    font-family: "Space Grotesk", sans-serif;
    font-size: 2rem;
    font-weight: 700;
}
.team-name {
    color: #ffffff;
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
}
.team-role {
    color: #cbd5e1;
    font-size: .86rem;
    margin-top: .3rem;
}
div[data-testid="stSidebar"] {
    background: #0b1220;
    border-right: 1px solid #475569;
}
div[data-testid="stSidebar"] * {
    color: #f5f7ff !important;
}
div[data-testid="stSidebar"] h1, div[data-testid="stSidebar"] h2,
div[data-testid="stSidebar"] h3 {
    font-family: "Space Grotesk", sans-serif !important;
    color: #ffffff !important;
}
div[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background: transparent !important;
    border: 1px solid #64748b !important;
    border-radius: 12px !important;
}
div[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
    background: transparent !important;
    border: 1px solid #94a3b8 !important;
    color: #ffffff !important;
}
.stButton > button {
    border-radius: 10px;
    border: 1px solid #d9d5f5;
}
</style>
""", unsafe_allow_html=True)

# ---------- Helpers ----------
@st.cache_data
def load_csv(file_bytes, name):
    import io
    return pd.read_csv(io.BytesIO(file_bytes))

def engineered_view(df):
    data = df.copy()
    if "PassengerId" in data:
        data["GroupId"] = data["PassengerId"].astype(str).str.split("_").str[0]
        data["GroupSize"] = data["GroupId"].map(data["GroupId"].value_counts())
    if "Cabin" in data:
        parts = data["Cabin"].fillna("Unknown/Unknown/Unknown").str.split("/")
        data["CabinDeck"] = parts.str[0]
        data["CabinNumber"] = pd.to_numeric(parts.str[1], errors="coerce")
        data["CabinSide"] = parts.str[2]
    spending = [c for c in ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"] if c in data]
    if spending:
        data["TotalSpending"] = data[spending].fillna(0).sum(axis=1)
        data["HasSpending"] = (data["TotalSpending"] > 0).astype(int)
    if "Age" in data:
        data["AgeGroup"] = pd.cut(
            data["Age"], bins=[-1, 12, 17, 25, 40, 60, np.inf],
            labels=["Child", "Teen", "Young adult", "Adult", "Middle age", "Senior"]
        )
    return data

def metric_card(label, value, note=""):
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">{label}</div>'
        f'<div class="metric-value">{value}</div>'
        f'<div class="metric-note">{note}</div></div>',
        unsafe_allow_html=True,
    )

def finish_chart(fig, margin_top=60):
    """Apply the site's dark, high-contrast styling to a Plotly chart."""
    fig.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="#f8fafc"),
        margin=dict(t=margin_top, b=30, l=30, r=30),
        legend=dict(font=dict(color="#f8fafc")),
    )
    fig.update_xaxes(gridcolor="#334155", zerolinecolor="#475569")
    fig.update_yaxes(gridcolor="#334155", zerolinecolor="#475569")
    return fig

def find_team_photo(member):
    """Find a team photo despite differences in filename or image extension."""
    team_dir = Path(__file__).parent / "assets" / "team"
    if not team_dir.exists():
        return None

    supported_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    preferred = team_dir / member["photo"]
    if preferred.exists():
        return preferred

    # Match files such as Hasti.png, hasti_photo.jpeg, or Thuy An Nguyen.jpg.
    filename_candidates = [
        path for path in team_dir.iterdir()
        if path.is_file() and path.suffix.lower() in supported_extensions
    ]
    name_tokens = [
        re.sub(r"[^a-z0-9]", "", token.lower())
        for token in member["name"].split()
    ]
    for path in filename_candidates:
        normalized_filename = re.sub(r"[^a-z0-9]", "", path.stem.lower())
        if any(token and token in normalized_filename for token in name_tokens):
            return path
    return None

def team_member_card(member):
    """Display a team member photo when it exists, otherwise show initials."""
    photo_path = find_team_photo(member)
    if photo_path is not None and photo_path.exists():
        st.image(str(photo_path), width=120)
    else:
        st.markdown(
            f'<div class="team-initials">{member["initials"]}</div>',
            unsafe_allow_html=True,
        )
    st.markdown(
        f'<div class="team-name">{member["name"]}</div>'
        f'<div class="team-role">{member["role"]}</div>',
        unsafe_allow_html=True,
    )

logo_path = Path(__file__).parent / "assets" / "tensorflowed_logo.png"
if logo_path.exists():
    logo_base64 = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    logo_html = (
        '<img class="hero-logo" '
        f'src="data:image/png;base64,{logo_base64}" alt="TensorFlowed logo">'
    )
else:
    logo_html = ""

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## Mission setup")
    st.caption("Load the project files to activate the interactive showcase.")

    train_file = st.file_uploader("Upload train.csv", type="csv")
    test_file = st.file_uploader("Upload test.csv", type="csv")
    comparison_file = st.file_uploader(
        "Optional: model comparison CSV", type="csv",
        help="Upload nov_8_model_comparison.csv or another CSV with Model and Validation Accuracy columns."
    )
    submission_file = st.file_uploader(
        "Optional: final submission CSV", type="csv"
    )

    st.divider()
    st.markdown("### Project results")
    baseline_score = st.number_input(
        "Original baseline score",
        min_value=0.0, max_value=1.0, value=0.79120, format="%.5f"
    )
    final_score = st.number_input(
        "Final Kaggle score",
        min_value=0.0, max_value=1.0, value=0.80734, format="%.5f"
    )
    st.caption("These values appear on the Results page and can be updated after your final submission.")

# ---------- Data ----------
if train_file is not None:
    train = load_csv(train_file.getvalue(), train_file.name)
else:
    train = None

if test_file is not None:
    test = load_csv(test_file.getvalue(), test_file.name)
else:
    test = None

comparison = None
if comparison_file is not None:
    comparison = load_csv(comparison_file.getvalue(), comparison_file.name)

submission = None
if submission_file is not None:
    submission = load_csv(submission_file.getvalue(), submission_file.name)

# ---------- Navigation ----------
st.markdown(f"""
<div class="hero">
    {logo_html}
    <div class="hero-content">
        <div class="badge">sheCodes SLP 2026 - Data Science</div>
        <h1>TensorFlowed</h1>
        <p>Turning passenger data into predictions: our machine learning journey through the Spaceship Titanic competition.</p>
    </div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "Navigate the showcase",
    ["Mission Control", "Data Explorer", "Model Arena", "About Us"],
    horizontal=True,
    label_visibility="collapsed",
)

if train is None:
    st.markdown('<div class="section-label">Start here</div>', unsafe_allow_html=True)
    st.info("Upload train.csv in the sidebar to activate the interactive charts. You can still explore the project story below.")
    st.markdown("### Our project in one sentence")
    st.markdown(
        '<div class="story-card"><strong>We built and compared machine learning models to predict whether passengers aboard the Spaceship Titanic were transported to another dimension.</strong></div>',
        unsafe_allow_html=True,
    )

# ---------- Mission Control ----------
if page == "Mission Control":
    st.markdown('<div class="section-label">Mission summary</div>', unsafe_allow_html=True)
    st.subheader("From raw data to a Kaggle submission")
    st.write(
        "Our project followed a complete data science pipeline: we understood the competition, explored the dataset, engineered features, prepared the data, trained models, evaluated predictions, and created a final submission."
    )

    if train is not None:
        transported_rate = train["Transported"].mean() if "Transported" in train else 0
        improvement = final_score - baseline_score
        cols = st.columns(4)
        with cols[0]:
            metric_card("Training passengers", f"{len(train):,}", "labeled examples")
        with cols[1]:
            metric_card("Input columns", f"{train.shape[1] - 1}", "before engineering")
        with cols[2]:
            metric_card("Transported", f"{transported_rate:.1%}", "training-set rate")
        with cols[3]:
            metric_card("Score improvement", f"+{improvement:.3f}", "over original baseline")
    else:
        cols = st.columns(4)
        for col, label, value, note in zip(
            cols,
            ["Project focus", "Data type", "Target", "Pipeline"],
            ["Machine learning", "Tabular", "Transported", "End-to-end"],
            ["Kaggle competition", "Passenger records", "Binary outcome", "Explore → submit"],
        ):
            with col:
                metric_card(label, value, note)

    st.markdown('<div class="section-label">Our pipeline</div>', unsafe_allow_html=True)
    pipeline = [
        ("01", "Understand", "Competition, rows, features, target"),
        ("02", "Prepare", "Missing values and categorical data"),
        ("03", "Engineer", "Cabin, group, spending, and age features"),
        ("04", "Model", "Compare classification algorithms"),
        ("05", "Evaluate", "Validation, charts, and Kaggle score"),
    ]
    pcols = st.columns(5)
    for col, (num, title, body) in zip(pcols, pipeline):
        with col:
            st.markdown(
                f'<div class="story-card"><strong>{num} · {title}</strong><br><small>{body}</small></div>',
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-label">What makes this a data science project?</div>', unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        st.markdown("### Questions we investigated")
        st.markdown("- Which passenger characteristics are associated with transportation?")
        st.markdown("- Which engineered features help a model make predictions?")
        st.markdown("- Which model performs best on unseen validation data?")
    with b:
        st.markdown("### What we produced")
        st.markdown("- A cleaned and engineered dataset")
        st.markdown("- Multiple trained classification models")
        st.markdown("- Presentation-ready visualizations")
        st.markdown("- A Kaggle submission file")

# ---------- About Us ----------
elif page == "About Us":
    st.markdown('<div class="section-label">Meet the team</div>', unsafe_allow_html=True)
    st.subheader("The people behind TensorFlowed")
    st.write(
        "We are a student data science team who worked together to explore the Spaceship Titanic competition and learn the machine learning process from start to finish."
    )

    team = [
        {
            "name": "Hasti Abbasi Kenarsari",
            "role": "Team Lead · 4th Year Computer Science and Data Science",
            "initials": "HA",
            "photo": "hasti.png",
        },
        {
            "name": "Athalia Zhou",
            "role": "4th Year Computer Science",
            "initials": "AZ",
            "photo": "athalia.png",
        },
        {
            "name": "Jaqueline Lopez",
            "role": "4th Year Applied Mathematics",
            "initials": "JL",
            "photo": "jaqueline.png",
        },
        {
            "name": "Thuy An Nguyen",
            "role": "4th Year Computer Science",
            "initials": "TN",
            "photo": "thuy-an.png",
        },
        {
            "name": "Mari Astillero",
            "role": "3rd Year Computer Science",
            "initials": "MA",
            "photo": "mari.png",
        },
    ]

    first_row = st.columns(3)
    for col, member in zip(first_row, team[:3]):
        with col:
            st.markdown('<div class="team-card">', unsafe_allow_html=True)
            team_member_card(member)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    second_row = st.columns([1, 1, 1])
    for col, member in zip([second_row[0], second_row[2]], team[3:]):
        with col:
            st.markdown('<div class="team-card">', unsafe_allow_html=True)
            team_member_card(member)
            st.markdown('</div>', unsafe_allow_html=True)

    st.caption(
        "To add photos, place hasti.png, athalia.png, jaqueline.png, thuy-an.png, and mari.png inside assets/team."
    )

# ---------- Data Explorer ----------
elif page == "Data Explorer":
    st.markdown('<div class="section-label">Explore the evidence</div>', unsafe_allow_html=True)
    st.subheader("What patterns exist in the passenger data?")

    if train is None:
        st.warning("Upload train.csv in the sidebar to view the charts.")
    else:
        data = engineered_view(train)
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Outcomes", "Passenger patterns", "Spending", "Relationships"]
        )

        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                outcome = data["Transported"].map({True: "Transported", False: "Not transported"}).value_counts()
                fig = px.pie(
                    values=outcome.values, names=outcome.index, hole=.58,
                    color=outcome.index,
                    color_discrete_map={"Transported": "#35c2c9", "Not transported": "#ef8bc8"},
                    title="Passenger outcomes"
                )
                fig.update_layout(showlegend=True, margin=dict(t=60, b=20, l=20, r=20))
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                if "CryoSleep" in data:
                    rates = pd.crosstab(
                        data["CryoSleep"].fillna("Missing"),
                        data["Transported"],
                        normalize="index"
                    ).reset_index()
                    rates = rates.rename(columns={True: "Transported", False: "Not transported"})
                    long = rates.melt(id_vars="CryoSleep", var_name="Outcome", value_name="Rate")
                    fig = px.bar(
                        long, x="CryoSleep", y="Rate", color="Outcome",
                        barmode="stack", text_auto=".0%",
                        color_discrete_map={"Transported": "#35c2c9", "Not transported": "#ef8bc8"},
                        title="Transportation rate by CryoSleep"
                    )
                    fig.update_yaxes(tickformat=".0%")
                    fig.update_layout(margin=dict(t=60, b=20, l=20, r=20))
                    st.plotly_chart(fig, use_container_width=True)

            c1, c2 = st.columns(2)
            with c1:
                if "HomePlanet" in data:
                    planet_rates = (
                        data.assign(HomePlanet=data["HomePlanet"].fillna("Missing"))
                        .groupby("HomePlanet")["Transported"]
                        .mean()
                        .mul(100)
                        .sort_values(ascending=False)
                        .reset_index(name="Transported")
                    )
                    fig = px.bar(
                        planet_rates, x="HomePlanet", y="Transported",
                        text=planet_rates["Transported"].map(lambda x: f"{x:.0f}%"),
                        color="Transported",
                        color_continuous_scale=["#b6edf0", "#7157d9"],
                        title="Transportation rate by home planet",
                    )
                    fig.update_layout(coloraxis_showscale=False, yaxis_title="Transported (%)")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)
            with c2:
                if "Destination" in data:
                    destination = (
                        data.assign(Destination=data["Destination"].fillna("Missing"))
                        .groupby("Destination")["Transported"]
                        .mean()
                        .mul(100)
                        .sort_values(ascending=False)
                        .reset_index(name="Transported")
                    )
                    fig = px.bar(
                        destination, x="Destination", y="Transported",
                        text=destination["Transported"].map(lambda x: f"{x:.0f}%"),
                        color="Transported",
                        color_continuous_scale=["#f6a8d5", "#7157d9"],
                        title="Transportation rate by destination",
                    )
                    fig.update_layout(coloraxis_showscale=False, yaxis_title="Transported (%)")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)

        with tab2:
            c1, c2 = st.columns(2)
            with c1:
                if "CabinDeck" in data:
                    deck = data.groupby("CabinDeck", dropna=False)["Transported"].mean().reset_index()
                    deck["Transported"] = deck["Transported"] * 100
                    fig = px.bar(
                        deck, x="CabinDeck", y="Transported",
                        color="Transported", color_continuous_scale=["#dfe8ff", "#7157d9"],
                        text=deck["Transported"].map(lambda x: f"{x:.0f}%"),
                        title="Transportation rate by cabin deck"
                    )
                    fig.update_layout(coloraxis_showscale=False, yaxis_title="Transported (%)", margin=dict(t=60, b=20, l=20, r=20))
                    st.plotly_chart(fig, use_container_width=True)
            with c2:
                if "AgeGroup" in data:
                    age = data.groupby("AgeGroup", observed=False)["Transported"].mean().reset_index()
                    age["Transported"] = age["Transported"] * 100
                    fig = px.line(
                        age, x="AgeGroup", y="Transported", markers=True,
                        title="Transportation rate across age groups"
                    )
                    fig.update_traces(line_color="#7157d9", marker_color="#35c2c9", marker_size=12)
                    fig.update_layout(yaxis_title="Transported (%)", margin=dict(t=60, b=20, l=20, r=20))
                    st.plotly_chart(fig, use_container_width=True)

            c1, c2 = st.columns(2)
            with c1:
                if "Age" in data:
                    age_plot = data.copy()
                    age_plot["Outcome"] = age_plot["Transported"].map(
                        {True: "Transported", False: "Not transported"}
                    )
                    fig = px.histogram(
                        age_plot.dropna(subset=["Age"]), x="Age", color="Outcome",
                        nbins=24, barmode="overlay", opacity=.72,
                        color_discrete_map={
                            "Transported": "#35c2c9",
                            "Not transported": "#ef8bc8",
                        },
                        title="Age distribution by outcome",
                    )
                    fig.update_layout(yaxis_title="Passenger count")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)
            with c2:
                if "CabinSide" in data:
                    side = (
                        data.assign(CabinSide=data["CabinSide"].fillna("Missing"))
                        .groupby("CabinSide")["Transported"]
                        .mean()
                        .mul(100)
                        .reset_index(name="Transported")
                    )
                    fig = px.bar(
                        side, x="CabinSide", y="Transported",
                        text=side["Transported"].map(lambda x: f"{x:.0f}%"),
                        color="CabinSide",
                        color_discrete_sequence=["#35c2c9", "#ef8bc8", "#b8a8ff"],
                        title="Transportation rate by cabin side",
                    )
                    fig.update_layout(showlegend=False, yaxis_title="Transported (%)")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)

            if "GroupSize" in data:
                group_plot = data.copy()
                group_plot["Outcome"] = group_plot["Transported"].map(
                    {True: "Transported", False: "Not transported"}
                )
                group_counts = (
                    group_plot.groupby(["GroupSize", "Outcome"])
                    .size()
                    .reset_index(name="Passengers")
                )
                fig = px.bar(
                    group_counts, x="GroupSize", y="Passengers", color="Outcome",
                    barmode="group",
                    color_discrete_map={
                        "Transported": "#35c2c9",
                        "Not transported": "#ef8bc8",
                    },
                    title="Passenger group size and outcome",
                )
                fig.update_layout(xaxis_title="Passengers in group", yaxis_title="Passenger count")
                st.plotly_chart(finish_chart(fig), use_container_width=True)

        with tab3:
            if "TotalSpending" in data:
                spend = data[["TotalSpending", "Transported"]].copy()
                spend["Outcome"] = spend["Transported"].map({True: "Transported", False: "Not transported"})
                fig = px.box(
                    spend, x="Outcome", y="TotalSpending", color="Outcome",
                    points=False, log_y=True,
                    color_discrete_map={"Transported": "#35c2c9", "Not transported": "#ef8bc8"},
                    title="Passenger spending by outcome"
                )
                fig.update_layout(showlegend=False, yaxis_title="Total spending (log scale)", margin=dict(t=60, b=20, l=20, r=20))
                st.plotly_chart(fig, use_container_width=True)

                spending_cols = [
                    c for c in ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
                    if c in data
                ]
                if spending_cols:
                    average_spend = (
                        data[spending_cols].fillna(0).mean()
                        .sort_values(ascending=False)
                        .rename("Average spending")
                        .reset_index()
                        .rename(columns={"index": "Category"})
                    )
                    average_spend["Category"] = average_spend["Category"].str.replace(
                        "([a-z])([A-Z])", r"\1 \2", regex=True
                    )
                    fig = px.bar(
                        average_spend, x="Category", y="Average spending",
                        color="Average spending",
                        color_continuous_scale=["#b6edf0", "#7157d9"],
                        title="Average spending by category",
                    )
                    fig.update_layout(coloraxis_showscale=False, yaxis_title="Average amount")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)

                if "HasSpending" in data:
                    spending_rate = (
                        data.assign(Spending=data["HasSpending"].map({1: "Any spending", 0: "No spending"}))
                        .groupby("Spending")["Transported"]
                        .mean()
                        .mul(100)
                        .reset_index(name="Transported")
                    )
                    fig = px.bar(
                        spending_rate, x="Spending", y="Transported",
                        text=spending_rate["Transported"].map(lambda x: f"{x:.0f}%"),
                        color="Spending",
                        color_discrete_map={"Any spending": "#35c2c9", "No spending": "#ef8bc8"},
                        title="Transportation rate by spending behavior",
                    )
                    fig.update_layout(showlegend=False, yaxis_title="Transported (%)")
                    st.plotly_chart(finish_chart(fig), use_container_width=True)

        with tab4:
            st.markdown("### How do numeric variables relate to the outcome?")
            numeric_candidates = [
                c for c in [
                    "Age", "RoomService", "FoodCourt", "ShoppingMall", "Spa",
                    "VRDeck", "TotalSpending", "GroupSize", "Transported"
                ] if c in data
            ]
            if len(numeric_candidates) >= 3:
                numeric = data[numeric_candidates].copy()
                numeric["Transported"] = numeric["Transported"].astype(int)
                corr = numeric.corr(numeric_only=True)
                fig = px.imshow(
                    corr, text_auto=".2f", aspect="auto",
                    color_continuous_scale=["#ef8bc8", "#0f172a", "#35c2c9"],
                    zmin=-1, zmax=1, title="Correlation matrix of numeric variables",
                )
                st.plotly_chart(finish_chart(fig), use_container_width=True)

            if {"Age", "TotalSpending"}.issubset(data.columns):
                relationship = data[["Age", "TotalSpending", "Transported"]].dropna().copy()
                relationship["Outcome"] = relationship["Transported"].map(
                    {True: "Transported", False: "Not transported"}
                )
                fig = px.scatter(
                    relationship, x="Age", y="TotalSpending", color="Outcome",
                    opacity=.55, hover_data=["Age", "TotalSpending"],
                    color_discrete_map={
                        "Transported": "#35c2c9",
                        "Not transported": "#ef8bc8",
                    },
                    title="Age, spending, and transportation outcome",
                )
                fig.update_yaxes(title="Total spending", type="log")
                st.plotly_chart(finish_chart(fig), use_container_width=True)

# ---------- Model Arena ----------
elif page == "Model Arena":
    st.markdown('<div class="section-label">Compare the competitors</div>', unsafe_allow_html=True)
    st.subheader("Which model learned the passenger patterns best?")
    st.write("The model comparison shows how different algorithms performed on the same prepared data.")

    if comparison is not None and {"Model", "Validation Accuracy"}.issubset(comparison.columns):
        results = comparison.copy().sort_values("Validation Accuracy", ascending=True)
        fig = px.bar(
            results, x="Validation Accuracy", y="Model", orientation="h",
            text=results["Validation Accuracy"].map(lambda x: f"{x:.3f}"),
            color="Validation Accuracy",
            color_continuous_scale=["#b6edf0", "#7157d9"],
            title="Validation accuracy by model"
        )
        fig.update_layout(coloraxis_showscale=False, xaxis_range=[.70, .85], margin=dict(t=60, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
        best = results.iloc[-1]
        st.success(f"Best validation model: {best['Model']} ({best['Validation Accuracy']:.3f})")
    else:
        st.info("Upload a model comparison CSV in the sidebar. It should contain columns named Model and Validation Accuracy.")
        st.markdown("### Models used in our project")
        model_cols = st.columns(3)
        for col, name, description in zip(
            model_cols,
            ["Logistic Regression", "Random Forest", "XGBoost"],
            ["Simple, interpretable baseline", "Many decision trees combined", "Sequential boosted trees"]
        ):
            with col:
                st.markdown(f'<div class="story-card"><strong>{name}</strong><br><small>{description}</small></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">How to explain the result</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="story-card">We compared multiple models using the same validation process, then used the strongest approach to generate our final Kaggle submission. The goal was not just to train a model, but to understand how preparation, feature engineering, and model choice work together.</div>',
        unsafe_allow_html=True,
    )


