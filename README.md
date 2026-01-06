# UCT Quantum Computing Society Website

Official website of the **University of Cape Town Quantum Computing Society (UCT QCS)**.

This platform serves as the central hub for our community, bridging the gap between academia and the quantum revolution in Africa. It showcases our events, research, and membership opportunities.

## ✨ Features

*   **🏠 Home:** Overview of the society, our mission to advocate for Quantum Computing in Africa, and our partnership with IBM Research.
*   **📅 Events:** Calendar and detailed list of upcoming Educational Talks, Socials, and Hackathons.
*   **👥 Community Dashboard:** Meet the 2026 Committee and explore member statistics and distributions.
*   **📰 Research Highlights:** Read our latest blog posts and research papers on Quantum Computing (e.g., AI in QC).
*   **📝 Membership:** Easy sign-up portal for prospective members.

## 🛠️ Tech Stack

*   **Framework:** [Streamlit](https://streamlit.io/)
*   **Language:** Python 3.x
*   **Data Visualization:** Plotly Express
*   **Data Handling:** Pandas

## ⚙️ Setup & Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/qcs-web.git
    cd qcs-web
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run home.py
    ```

## 📂 Project Structure

```
qcs-web/
├── home.py                 # Entry point / Landing page
├── pages/                  # Multi-page application pages
│   ├── 02_Events.py
│   ├── 03_Members.py
│   ├── 04_Blog.py
│   └── 05_About.py
├── data/                   # JSON and CSV data stores
├── assets/                 # Images and CSS files
├── utils/                  # Helper functions
└── requirements.txt        # Python dependencies
```

## 📬 Contact

Connect with us:
*   [Instagram](https://instagram.com)
*   [LinkedIn](https://www.linkedin.com/company/uct-qcs)
*   [YouTube](https://www.youtube.com/@UCTQCS)

&copy; 2026 UCT Quantum Computing Society.
