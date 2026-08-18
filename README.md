<div align="center">
<h3 align="center">IoT Behaviour Extractor</h3>

  <p align="center">
    A script to extact behaviour of smart devices from IoT platforms repositories
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#known-bugs">Known Bugs</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# About the project

This project was done as a part of McGill University's Summer Undergraduate Research in Engineering (SURE) 2026.

There is often difficulty in IoT software testing, with an observed average statement coverage of 65.2%, branch coverage of 53.5%, and mutation score of 39.9% from studied IoT projects. An automated testing suite can help improve these testing scores within IoT software.Simulated smart devices would allow for a behavioural testing procedure across multiple IoT platforms, foregoing differences in programming language, communication protocols and architecture. In order to do this, the expected behaviour of the devices need to be understood to accurately depict the response it will have to certain commands.

The idea behind this project is to extract this behavioural information from existing test cases on the open source IoT repositories, which can be used later on for evaluating the simulated hardware.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/matt-yst/SURE-2026.git
   ```
2. Navigate to the project directory
3. Create Python virtual environment
   ```sh
   python -m venv .venv
   ```
4. Activate the virtual environment

    <b>Windows</b>
   ```sh
   .venv\Scripts\activate.bat
   ```
   <b>MacOS/ Linux</b>
    ```sh
   source .venv/bin/activate
   ```
5. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Usage

The main script is src/docs_parser/repo_parser.py

To run the script, you can run the command

   ```sh
   python3 src/docs_parser/repo_parser.py
   ```
You will need to clone the Home Assitant repository into a sibling directory before running the script. Ensure that the Pathlib directory in the script is pointing to the correct IoT platform directory that you cloned. 

It is important to note that the script relies on a locally hosted LLM, right now it is configured to use Ollama gpt-oss(120b). If you do not have access to this model locally or otherwise, do reconfigure it yourself to use the model of your choice.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Known Bugs
In its current iteration, there are times where the LLM can be inaccurate in its output representation of the device behaviour. The most common error is missing information due to the lack of classification of assert statements. Further improvements will be made to the pre-processing of the input data with the exploration of Python's AST module. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contact
Want to discuss further about this project? You can contact me through these means:

email - matthew.y.tan@mail.mcgill.ca
LinkedIn - https://www.linkedin.com/in/matt-yst/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Acknowledgements

Thank you to Rufeng Chen, Dr. Lili Wei and Dr. Steven Ding for your support throughout this project. I would not have been able to accomplish it without your help.

