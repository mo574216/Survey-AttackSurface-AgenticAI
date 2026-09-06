# The Expanding Attack Surface of Agentic AI: Vulnerabilities, Threat Models, Defenses, and Benchmarks

This repository contains the complete LaTeX source code, figures, tables, bibliography, and compiled PDF manuscripts for the survey paper:

> **The Expanding Attack Surface of Agentic AI: Vulnerabilities, Threat Models, Defenses, and Benchmarks**  
> **Author:** Seyedakbar Mostafavi  
> **Affiliation:** Department of Computer Engineering, Yazd University, Yazd, Iran  
> **Contact:** [a.mostafavi@yazd.ac.ir](mailto:a.mostafavi@yazd.ac.ir)

---

## 📄 Manuscript Formats & Compiled Results

The paper is maintained in two publication-ready formats:

1. **ACM Computing Surveys (CSUR) Format:**
   - Source: [`acm_main.tex`](acm_main.tex) (uses `acmart.cls` with `acmsmall` option)
   - Compiled PDF: [`acm_main.pdf`](acm_main.pdf) (29 pages)
   - Adheres to ACM CSUR single-column survey guidelines with in-depth analysis, comprehensive tables, and modular taxonomy.

2. **IEEE Transactions Format:**
   - Source: [`main.tex`](main.tex) (uses `IEEEtran.cls`)
   - Compiled PDF: [`main.pdf`](main.pdf) (16 pages)
   - Formatted to strict 16-page double-column IEEE Transactions standard (TDSC/TIFS profile).

---

## 🗂 Repository Structure

```
├── acm_main.tex          # ACM Computing Surveys master document
├── acm_main.pdf          # Compiled ACM format PDF
├── main.tex              # IEEE Transactions master document
├── main.pdf              # Compiled IEEE format PDF (16 pages)
├── references.bib        # Verified bibliography database (73 grounded entries)
├── sections/             # Modular section files
│   ├── 00_abstract.tex
│   ├── 01_introduction.tex
│   ├── 02_architecture.tex
│   ├── 03_threat_model.tex
│   ├── 04_attack_taxonomy.tex
│   ├── 05_modality_mcp.tex
│   ├── 06_multi_agent.tex
│   ├── 07_defenses.tex
│   ├── 08_benchmarks_metrics.tex
│   ├── 09_standards_governance.tex
│   ├── 10_open_challenges.tex
│   └── 11_conclusion.tex
├── figures/              # Publication-grade vector TikZ figures
│   ├── fig_architecture.tex       # Agentic AI Reference Architecture
│   ├── fig_causal_graph.tex       # Causal Structural Equation Attack Graph
│   ├── fig_mcp_architecture.tex   # Model Context Protocol (MCP) Trust Boundaries & Threats
│   ├── fig_mas_topologies.tex     # Multi-Agent System Topologies (Orchestrator, Swarm, Blackboard)
│   └── fig_defense_layers.tex     # Defense-in-Depth Mitigation Framework
├── tables/               # Formatted LaTeX tables
│   ├── tab_nomenclature.tex       # Formal Mathematical Symbols & Definitions
│   ├── tab_attack_taxonomy.tex    # Cross-Layer Attack Taxonomy Matrix
│   ├── tab_defense_matrix.tex     # Defense-in-Depth Evaluation Matrix
│   ├── tab_benchmarks.tex         # Empirical Security Benchmarks & Datasets
│   └── tab_standards_mapping.tex  # Regulatory & Framework Mapping (OWASP, MITRE, EU AI Act, NIST)
└── base_paper/           # Reference base preprints
```

---

## 🛠 Compilation Instructions

To build the PDF documents locally using TeX Live / MiKTeX:

### Building ACM CSUR Format:
```bash
pdflatex -interaction=nonstopmode acm_main.tex
bibtex acm_main
pdflatex -interaction=nonstopmode acm_main.tex
pdflatex -interaction=nonstopmode acm_main.tex
```

### Building IEEE Transactions Format:
```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## ⚖ Citation

If you find this survey or repository useful in your research, please cite:

```bibtex
@article{mostafavi2026expandingsurvey,
  title={The Expanding Attack Surface of Agentic AI: Vulnerabilities, Threat Models, Defenses, and Benchmarks},
  author={Mostafavi, Seyedakbar},
  journal={ACM Computing Surveys / IEEE Transactions on Dependable and Secure Computing},
  year={2026}
}
```
