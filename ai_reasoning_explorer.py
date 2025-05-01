import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="AI Reasoning Explorer", layout="wide")

# App title and description
st.title("🧠 AI Reasoning Explorer")
st.markdown("""
This app demonstrates advanced reasoning capabilities in modern AI models,
showcasing how 2025's AI systems approach complex problem-solving.
""")

# Sidebar for model selection
st.sidebar.header("Model Configuration")
model_type = st.sidebar.selectbox(
    "Select Reasoning Model Type", 
    ["Chain-of-Thought", "Tree of Thoughts", "Verification-Assisted", "Mathematical Reasoning"]
)

reasoning_depth = st.sidebar.slider("Reasoning Depth", 1, 10, 5)
confidence_threshold = st.sidebar.slider("Confidence Threshold (%)", 50, 99, 85) / 100

# Problem selection section
st.subheader("Select a Problem Type")

problem_categories = {
    "Logical Reasoning": [
        "If all A are B, and some B are C, what can we conclude about A and C?",
        "Given premises: If it rains, the ground gets wet. The ground is wet. Can we conclude it rained?",
        "If X speaks the truth, and X says that Y lies, and Y says that Z speaks the truth, does Z speak the truth?"
    ],
    "Mathematical Problem Solving": [
        "Find the value of x in the equation: 3x² + 6x - 24 = 0",
        "If a square has a perimeter of 20 units, what is its area?",
        "City A is 150 miles north of City B. A car travels from City A at 60 mph. Another car travels from City B at 40 mph. How long until they meet?"
    ],
    "Commonsense Reasoning": [
        "If I put an ice cube on a hot plate, what will happen and why?",
        "Why might someone take an umbrella when leaving their house in the morning?",
        "If a glass falls off a table onto a carpeted floor, is it more or less likely to break than on a tile floor?"
    ],
    "Counterfactual Reasoning": [
        "What would happen if gravity on Earth was suddenly half its current strength?",
        "How would history be different if the internet had been invented in the 1950s?",
        "What would transportation systems look like if fossil fuels had never been discovered?"
    ]
}

# Two-column layout for problem selection
col1, col2 = st.columns(2)

with col1:
    problem_category = st.selectbox("Problem Category", list(problem_categories.keys()))

with col2:
    problem = st.selectbox("Specific Problem", problem_categories[problem_category])

# Reasoning execution
if st.button("Generate Reasoning Process"):
    # Create containers for different parts of the output
    reasoning_container = st.container()
    with reasoning_container:
        st.subheader("AI Reasoning Process")
        process_placeholder = st.empty()
        
        # Different reasoning traces based on model type
        if model_type == "Chain-of-Thought":
            steps = []
            
            if problem_category == "Logical Reasoning":
                if "If all A are B" in problem:
                    steps = [
                        "First, let's clarify what we know: (1) All A are B, (2) Some B are C.",
                        "From statement (1), we know that every element in set A is also in set B.",
                        "From statement (2), we know that at least one element in set B is also in set C.",
                        "However, we don't know if that overlapping element between B and C is also in A.",
                        "Therefore, we can only conclude that *some A might be C*, but we cannot be certain.",
                        "The most logically valid conclusion is: Some A *may* be C, but it's not necessarily the case."
                    ]
                elif "If it rains" in problem:
                    steps = [
                        "Let's analyze the premises: (1) If it rains, the ground gets wet. (2) The ground is wet.",
                        "This follows the logical form: If P, then Q. We observe Q.",
                        "However, this is the fallacy of affirming the consequent.",
                        "While rain causes wet ground, other factors might also cause wet ground (sprinklers, water spill, etc.).",
                        "Therefore, we cannot conclusively determine that it rained.",
                        "The logical conclusion is: We cannot conclude with certainty that it rained."
                    ]
            elif problem_category == "Mathematical Problem Solving":
                if "3x²" in problem:
                    steps = [
                        "We need to solve the quadratic equation: 3x² + 6x - 24 = 0",
                        "First, I'll factor out a common factor of 3: 3(x² + 2x - 8) = 0",
                        "Now I need to factor the expression inside the parentheses: x² + 2x - 8",
                        "I'm looking for two numbers that multiply to -8 and add to 2",
                        "These numbers are 4 and -2, since 4 × (-2) = -8 and 4 + (-2) = 2",
                        "Therefore, x² + 2x - 8 = (x + 4)(x - 2)",
                        "So the original equation becomes: 3(x + 4)(x - 2) = 0",
                        "Setting each factor equal to zero: x + 4 = 0 or x - 2 = 0",
                        "Solving: x = -4 or x = 2",
                        "Therefore, x = -4 or x = 2 are the solutions to the equation."
                    ]
            
            # Display reasoning steps with animation
            full_text = ""
            for i, step in enumerate(steps):
                full_text += f"**Step {i+1}:** {step}\n\n"
                process_placeholder.markdown(full_text)
                time.sleep(0.7)  # Delay between steps
                
        elif model_type == "Tree of Thoughts":
            # Simulate tree-based reasoning
            st.markdown("### Exploring multiple reasoning paths:")
            
            cols = st.columns(3)
            
            # Display multiple reasoning paths
            for i in range(3):
                with cols[i]:
                    st.markdown(f"#### Path {i+1}")
                    for j in range(min(reasoning_depth, 4)):
                        with st.expander(f"Reasoning Step {j+1}", expanded=j==0):
                            if problem_category == "Counterfactual Reasoning":
                                if "gravity" in problem:
                                    paths = [
                                        [
                                            "Objects would feel lighter, requiring less force to lift",
                                            "Jumping would reach approximately twice the height",
                                            "Tall structures would need less support material",
                                            "Conclusion: More efficient construction but many physical adaptations needed"
                                        ],
                                        [
                                            "Water would flow differently, affecting rivers and tides",
                                            "Weather patterns would change due to atmospheric pressure differences",
                                            "Ecosystems would adapt to new physical environment",
                                            "Conclusion: Major environmental cascade effects"
                                        ],
                                        [
                                            "Human physiology would change over time due to less bone density needed",
                                            "Sports and physical activities would fundamentally change",
                                            "Transportation systems would be redesigned for different physics",
                                            "Conclusion: Society would reorganize around new physical constants"
                                        ]
                                    ]
                                    st.write(paths[i][j] if j < len(paths[i]) else "Further exploration...")
                            else:
                                st.write("Reasoning step content...")
                    
                    # Show confidence score for this path
                    confidence = random.uniform(0.65, 0.98)
                    st.progress(confidence)
                    st.write(f"Path confidence: {confidence:.2%}")
            
            # Final conclusion
            st.markdown("### Synthesized conclusion from highest-confidence paths:")
            if problem_category == "Counterfactual Reasoning" and "gravity" in problem:
                st.markdown("""
                With half the gravity, Earth would experience cascading effects across physical structures, 
                biological systems, and human society. Buildings could be taller, humans would experience 
                musculoskeletal changes over time, and natural systems like water flows and weather patterns 
                would fundamentally change. Transportation and sport would need to be reinvented.
                """)
                
        elif model_type == "Verification-Assisted":
            # Simulate verification-based reasoning
            if problem_category == "Mathematical Problem Solving" and "square has a perimeter" in problem:
                reasoning_steps = [
                    "Given: A square with perimeter = 20 units",
                    "Let's call the side length of the square 's'",
                    "Formula for perimeter of a square: 4s = 20",
                    "Solving for s: s = 20/4 = 5",
                    "Formula for area of a square: A = s²",
                    "Substituting: A = 5² = 25",
                    "Therefore, the area is 25 square units"
                ]
                
                verifications = [
                    "✓ Perimeter calculation is correct: 4 × 5 = 20",
                    "✓ Area calculation is correct: 5 × 5 = 25",
                    "✓ Units are appropriate: square units for area"
                ]
                
                # Display reasoning
                for i, step in enumerate(reasoning_steps):
                    st.markdown(f"**Step {i+1}:** {step}")
                    time.sleep(0.4)
                
                # Display verification
                st.markdown("### Verification Steps:")
                for check in verifications:
                    st.markdown(check)
                    time.sleep(0.4)
                
                # Display final answer with high confidence
                st.markdown("### Verified Answer:")
                st.markdown("The area of the square is **25 square units**")
                st.progress(0.99)
                st.markdown("Confidence: 99% (Verified)")
                
        elif model_type == "Mathematical Reasoning":
            if "City A" in problem:
                st.latex(r"\text{Given:}")
                st.latex(r"\text{- City A is 150 miles north of City B}")
                st.latex(r"\text{- Car 1 travels from City A at 60 mph}")
                st.latex(r"\text{- Car 2 travels from City B at 40 mph}")
                
                st.markdown("### Step-by-step solution:")
                time.sleep(0.5)
                st.latex(r"\text{Let's define variables:}")
                st.latex(r"\text{- Let t = time (in hours) until the cars meet}")
                time.sleep(0.5)
                st.latex(r"\text{Distance traveled by Car 1: } d_1 = 60t \text{ miles}")
                st.latex(r"\text{Distance traveled by Car 2: } d_2 = 40t \text{ miles}")
                time.sleep(0.5)
                st.latex(r"\text{Since the cars are traveling toward each other:}")
                st.latex(r"d_1 + d_2 = 150")
                time.sleep(0.5)
                st.latex(r"60t + 40t = 150")
                st.latex(r"100t = 150")
                st.latex(r"t = 1.5 \text{ hours}")
                time.sleep(0.5)
                st.markdown("### Answer:")
                st.markdown("The cars will meet after **1.5 hours** (or 1 hour and 30 minutes)")
    
    # Display model confidence and reasoning metrics
    metrics_container = st.container()
    with metrics_container:
        st.subheader("Model Performance Metrics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            confidence_score = random.uniform(max(0.75, confidence_threshold - 0.1), 0.98)
            st.metric("Confidence Score", f"{confidence_score:.2%}")
        
        with col2:
            st.metric("Reasoning Depth", f"{reasoning_depth}/10")
            
        with col3:
            reasoning_time = random.uniform(0.5, 3.0)
            st.metric("Processing Time", f"{reasoning_time:.2f} sec")
            
        # Simulate different uncertainty sources
        st.subheader("Uncertainty Analysis")
        uncertainty_data = {
            "Source": ["Premise Ambiguity", "Knowledge Gaps", "Logical Conflicts", "Counterfactual Uncertainty"],
            "Contribution": [random.uniform(0, 0.3), random.uniform(0, 0.2), 
                            random.uniform(0, 0.15), random.uniform(0, 0.35)]
        }
        
        uncertainty_df = pd.DataFrame(uncertainty_data)
        
        # Create horizontal bar chart
        fig, ax = plt.subplots(figsize=(10, 3))
        bars = ax.barh(uncertainty_df["Source"], uncertainty_df["Contribution"], color="skyblue")
        ax.set_xlim(0, 0.5)
        ax.set_xlabel("Uncertainty Contribution")
        ax.set_title("Sources of Reasoning Uncertainty")
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, f"{width:.2f}", 
                   ha='left', va='center')
            
        st.pyplot(fig)

# Information about reasoning models
with st.expander("About AI Reasoning Models in 2025"):
    st.markdown("""
    ### 2025 AI Reasoning Models
    
    **Chain-of-Thought:** Models break down problems into sequential reasoning steps, making thinking explicit and transparent. Used by OpenAI's o1 and GPT-5 models.
    
    **Tree of Thoughts:** Models explore multiple reasoning paths simultaneously, evaluating possibilities before converging on the most promising solutions. Used by DeepMind's advanced reasoning systems.
    
    **Verification-Assisted:** Models generate reasoning steps and then independently verify their correctness, improving accuracy on tasks requiring precision. Used in Google's Gemini Ultra models.
    
    **Mathematical Reasoning:** Specialized models with enhanced capabilities for symbolic manipulation, equation solving, and mathematical deduction. Used in scientific and engineering applications.
    
    The 2025 models show dramatic improvements in:
    - Multi-step reasoning consistency
    - Handling uncertainty and ambiguity
    - Self-correction capabilities
    - Integration of knowledge with logical operations
    """)

# References section
st.sidebar.markdown("---")
st.sidebar.markdown("""
### References
- What's next for AI in 2025 (MIT Technology Review)
- OpenAI o1 Model Documentation
- The State of AI 2025 (IEEE Spectrum)
- Morgan Stanley AI Trends Report 2025
""")
