# Multi-Agent LLM Pipeline for Automated Clinical Trial Data Extraction

This repository contains the code for a comparative analysis of multiple Large Language Models (LLMs) for automated clinical trial data extraction, with a focus on aging research and brain stimulation trials.

## 📋 Project Overview

Large Language Models have shown promise for automating evidence synthesis tasks like clinical trial data extraction, but comparative performance across different LLMs remains underexplored. This project evaluates how five state-of-the-art LLMs extract key elements from clinical trial protocols focusing on transcranial direct current stimulation (tDCS) in aging populations.

### Research Questions

1. How reliably can different LLMs extract structured information from unstructured clinical trial text?
2. Which LLMs perform best for specific types of information (categorical vs. numerical)?
3. How effective is a multi-agent approach compared to single-model extraction?
4. What level of human oversight is still required for automated data extraction?

## 🔄 Pipeline Architecture

The pipeline consists of three sequential stages:

### 1. Data Collection (`01_ct_pull.ipynb`)
- Connects to the ClinicalTrials.gov API (v2)
- Retrieves clinical trial data using aging-related search terms
- Implements pagination and comprehensive error handling
- Stores raw trial data in structured format

### 2. Data Filtering (`02_simple_filtering.ipynb`)
- Identifies trials relevant to brain stimulation using regex patterns
- Performs data cleaning and standardization
- Prepares filtered dataset for LLM processing
- Creates a focused dataset for deeper analysis

### 3. LLM Processing (`03_LLM_processor.ipynb`)
- Processes each trial through five different LLM models via OpenRouter
- Uses structured prompt engineering with JSON schema
- Extracts information including:
  - Brain stimulation presence (Yes/No)
  - Stimulation type (tDCS, TMS, etc.)
  - Target brain regions
  - Stimulation parameters (intensity, duration)
  - Model confidence levels
- Validates and compares outputs across models

## 🤖 Models Evaluated

The research compares five leading LLMs:

| Model | Provider | Parameters | Characteristics |
|-------|----------|------------|-----------------|
| o1-mini | OpenAI | - | Specialized for structured tasks |
| Grok-2-1212 | X-AI | - | Advanced reasoning capabilities |
| Llama-3.3-70b | Meta | 70B | Strong open-source performance |
| Gemini-Flash-1.5 | Google | 8B | Efficient with structured data |
| DeepSeek-R1 | DeepSeek | 70B | Optimized for scientific text |

All models are accessed through the OpenRouter API to standardize interaction patterns.

## 📊 Key Findings

Our analysis reveals:

- High agreement on categorical fields (brain stimulation presence: Fleiss' κ > 0.90)
- Moderate agreement on complex features (anatomical targets: κ ≈ 0.61)
- Varied performance on numeric parameters (session duration: ICC ≈ 0.35)
- No single model excels across all extraction tasks
- The multi-agent approach provides more reliable data than any single model

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Required libraries (see requirements.txt)
- OpenRouter API key

### Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/multi-agent-llm-pipeline.git
cd multi-agent-llm-pipeline
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
```bash
cp .env.example .env
# Edit .env to add your OpenRouter API key
```

### Running the Pipeline

Execute the notebooks in sequence:

1. Data Collection
```bash
jupyter notebook notebooks/01_ct_pull.ipynb
```

2. Data Filtering
```bash
jupyter notebook notebooks/02_simple_filtering.ipynb
```

3. LLM Processing
```bash
jupyter notebook notebooks/03_LLM_processor.ipynb
```

## 🧠 Prompt Engineering

The system employs a carefully designed prompt structure with:

1. Contextual information from the clinical trial
2. Clear instructions for extracting brain stimulation details
3. Structured JSON schema for standardized outputs
4. Example format for proper response construction

Example JSON schema:
```json
{
  "brain_stimulation_used": "Yes or No",
  "stimulation_details": {
    "primary_type": "e.g., tDCS, TMS, tACS, DBS, etc.",
    "is_noninvasive": true or false,
    "primary_target": "Primary brain region",
    "secondary_targets": ["List of secondary regions"],
    "stimulation_parameters": {
      "intensity": "e.g., 2mA",
      "duration": "e.g., 20 minutes"
    }
  },
  "confidence_level": "High, Medium, or Low",
  "relevant_quotes": ["Direct quotes supporting the analysis"]
}
```

## 📁 Repository Structure

```
.
├── notebooks/               # Jupyter notebooks for the pipeline
│   ├── 01_ct_pull.ipynb     # Data collection from ClinicalTrials.gov
│   ├── 02_simple_filtering.ipynb  # Trial filtering
│   └── 03_LLM_processor.ipynb     # LLM processing
├── src/                     # Source code
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── utils.py         # Core utilities for API calls, validation
├── data/                    # Data directory
│   └── sample_trials.csv    # Sample data for testing
├── results/                 # Directory for pipeline outputs
├── .env.example             # Template for environment variables
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 📝 Citation

If you use this code or methodology in your research, please cite:

```
Young, R., Matthews, A., & Poston, B. (2025). Comparative Analysis of Multi-Agent 
Large Language Models for Automated Clinical Trial Data Extraction in Aging Research.
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

- Richard Young (Primary Investigator)
- Alice Matthews
- Brach Poston

## 🤝 Acknowledgments

We thank OpenRouter for providing API access to multiple LLM models, enabling standardized comparisons across providers.