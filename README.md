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
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# About the project
---
This project was done as a part of McGill University's Summer Undergraduate Research in Engineering (SURE) 2026.

There is often difficulty in IoT software testing, with an observed average statement coverage of 65.2%, branch coverage of 53.5%, and mutation score of 39.9% from studied IoT projects. An automated testing suite can help improve these testing scores within IoT software.Simulated smart devices would allow for a behavioural testing procedure across multiple IoT platforms, foregoing differences in programming language, communication protocols and architecture. In order to do this, the expected behaviour of the devices need to be understood to accurately depict the response it will have to certain commands.

The idea behind this project is to extract this behavioural information from existing test cases on the open source IoT repositories, which can be used later on for evaluating the simulated hardware.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Getting Started
---
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
---
The main script is src/docs_parser/repo_parser.py

To run the script, you can run the command

   ```sh
   python3 src/docs_parser/repo_parser.py
   ```
You will need to clone the Home Assitant repository into a sibling directory before running the script. Ensure that the Pathlib directory in the script is pointing to the correct IoT platform directory that you cloned. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Known Bugs


