
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Careem Reputation Learning Engine", page_icon="🧠", layout="wide")

st.title("Careem Reputation Learning Engine")
st.caption("AI becomes the communications team's memory.")
st.caption("Prototype • Sample Data")

with st.sidebar:
    st.header("Intelligence Scope")
    segment = st.selectbox("Segment", ["Mobility & Delivery", "Food Delivery", "Payments"])
    st.selectbox("Market", ["UAE", "GCC"])
    st.markdown("---")
    st.write("**Learning loop**")
    st.write("Media + social → classify → compare action/reaction → learn → recommend")

st.header("Today's reputation intelligence")
st.subheader("Here are the three conversations you shouldn't ignore today.")

c1, c2, c3 = st.columns(3)
with c1:
    st.error("🚨 Airport pickup complaints increasing (+41%)")
    st.write("Competitors who acknowledged delays quickly were associated with faster sentiment recovery.")
    st.button("View recommended response", key="airport")
with c2:
    st.warning("⚠️ Driver safety discussion returning")
    st.write("In the last four similar demo incidents, humorous replies underperformed.")
    st.write("**Recommended tone:** Empathetic + factual")
with c3:
    st.success("🔥 Competitor campaign outperforming")
    st.write("A competitor post generated unusually high positive engagement with a similar audience.")
    st.button("Analyze why", key="campaign")

st.divider()
st.header("What the system is learning")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Issue Intelligence", "Media + Social", "Competitor Learning", "Weekly Intelligence"]
)

with tab1:
    st.subheader("Airport pickup")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Similar events", "12")
    m2.metric("Avg. recovery", "4.6 h")
    m3.metric("Best response pattern", "Acknowledge → explain → update")
    m4.metric("Evidence confidence", "High")
    st.markdown("### Historical lesson")
    st.write(
        "Across the demo event set, early acknowledgement followed by a clear explanation "
        "and continuing updates was associated with better recovery than silence or a single late statement."
    )
    st.markdown("### Suggested response")
    st.write(
        "We’re seeing longer pickup times at the airport and know this is frustrating. "
        "Our teams are working on the current congestion and we’ll keep customers updated as conditions change."
    )
    st.markdown("### Executive talking points")
    st.write("• Acknowledge the customer impact first\n\n• Explain the operational cause without defensiveness\n\n• Give only timelines the team can support")

with tab2:
    st.subheader("The system reads both media and social media")
    data = pd.DataFrame([
        ["News", "Careem", "Airport operations", "Neutral", "Operational disruption", "Monitor"],
        ["Instagram", "Careem", "Driver story", "Positive", "Human storytelling", "Repeat pattern"],
        ["X", "Competitor", "Payment outage", "Negative → recovering", "Frequent updates", "Benchmark"],
        ["News", "Competitor", "Sustainability", "Positive", "Executive proof points", "Analyze"],
        ["Instagram", "Competitor", "Campaign", "Positive", "High audience resonance", "Benchmark"],
    ], columns=["Source", "Brand", "Topic", "Reaction", "Observed action", "Learning status"])
    st.dataframe(data, use_container_width=True, hide_index=True)
    st.caption(
        "Production version would ingest permitted/licensed sources and client-owned data. "
        "This prototype uses self-created examples."
    )

with tab3:
    st.subheader("Action → reaction → lesson")
    st.markdown("""
**Pattern 01 — Service disruption**  
Action: early acknowledgement + explanation + repeated updates  
Observed reaction: lower escalation and faster recovery  
**Lesson:** communicate before the information vacuum grows.

**Pattern 02 — Driver stories**  
Action: real employee/driver storytelling  
Observed reaction: stronger positive engagement than promotional graphics  
**Lesson:** human proof performs better for this topic.

**Pattern 03 — Safety issue**  
Action: humorous response  
Observed reaction: weaker reception in repeated similar events  
**Lesson:** use empathetic + factual language for safety conversations.
""")
    st.caption("Associations in the demo are illustrative; production insights should distinguish correlation from causation.")

with tab4:
    st.subheader("This week we learned…")
    st.markdown("""
- Driver stories were associated with stronger positive engagement.
- Acknowledging a problem before explaining it reduced escalation in the demo history.
- Delivery-delay conversations rose alongside weather-related discussion.
- One competitor's frequent outage updates were associated with faster sentiment recovery.
""")
    st.markdown("### Next week's playbook")
    st.write("Acknowledge early → explain clearly → give a realistic timeline → continue updating.")
    st.success("Every communication becomes training data for the next communication.")

st.divider()
st.caption("Prototype concept: the system doesn't just tell you what happened; it tells you what was learned.")
