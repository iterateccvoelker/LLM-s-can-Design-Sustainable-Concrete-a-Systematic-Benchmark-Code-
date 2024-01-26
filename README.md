# LLMs in Sustainable Concrete Design: A Systematic Benchmark
## "Code, Data, Results"

### Authors:
- Christoph Völker *a
- Tehseen Rug b
- Kevin Maik Jablonka c
- Sabine Kruschwitz a,d

#### Affiliations:
- *a* Bundesanstalt für Materialforschung und -prüfung, Unter den Eichen 87, Berlin, Germany
- *b* Iteratec GmbH, St.-Martin-Str. 114, 81669 Munich, Germany
- *c* Helmholtz Institute for Polymers in Energy Applications, Jena, Germany
- *d* Technische Universität Berlin, Institute of Civil Engineering, Non-destructive building material testing, Gustav-Meyer-Allee 25, 13355 Berlin, Germany

### Abstract:
In the context of a circular building material economy, the complexity of resource flows and the variability of material composition pose significant challenges. This study demonstrates how Large Language Models (LLMs) can advance material design by adopting a Knowledge-Driven Design (KDD) approach that outperforms traditional Data-Driven Design (DDD) methods. Our focus is on designing alkali-activated concrete (AAC) mix designs, an environmentally friendly alternative to conventional Portland cement-based concrete. GPT-3.5 Turbo and GPT-4 Turbo enable using fuzzy design knowledge as previously untapped input data modality. A key aspect of our research is to improve the performance of the LLMs in post-training. We use strategies such as refining prompt context, extending test time, and including a verifier.The study's systematic benchmarks are based on 240 AAC formulations extracted from the literature. The target was on achieving maximum compressive strength through an adaptive design approach over multiple development cycles. We compare these results to the traditional DDD baseline methods. KDD outperforms conventional methods by providing robust initial predictions and demonstrating effective adaptability informed by laboratory validation data, culminating in the development of high-quality AAC formulations. These results provide valuable insight into the capabilities of chat-based LLMs in managing complex material formulations, which are particularly beneficial in situations where traditional DDD is impractical due to data collection issues.  With natural language as the basis the KDD is intuitively accessible to domain experts.  The methodology and results of this study have significant implications for the field of materials science, particularly in the context of a circular economy, and pave the way for innovative applications of LLMs in various scientific fields.

### Repository Structure:
- `Data/`: Contains the datasets used in the benchmarking.
- `Results/`: Stores the generated results.
- `Prompts/`: Includes the prompts used for interacting with the LLMs.
- `Utils/`: Contains utility scripts for setting configurations and running experiments.
- `Benchmarking.ipynb`: The main script for configuring and executing experiments via IPython widgets. Run each cell successively to utilize utility scripts from the `Utils/` folder.
- `PlotResults`: Script for selecting and visualizing results as line plots or tables, replicating figures from the manuscript.

### Usage Instructions:
1. **Setup**: Clone the repository and install necessary dependencies (listed in `requirements.txt`).
2. **Running Experiments**: Open `Benchmarking.ipynb` and configure experiments using IPython widgets. Run each cell in sequence.
3. **Visualizing Results**: Use `PlotResults` to select results from the `Results/` folder and visualize them as per your requirement.

### Contributing:
Contributions to this project are welcome. Please refer to the `CONTRIBUTING.md` file for guidelines.

### License:
This project is licensed under the [MIT License](LICENSE).

### Citation:
For citing this work in academic papers, please refer to the citation format provided in `CITATION.md`.

### Contact:
For further inquiries or collaboration, please contact [Author's Email].


