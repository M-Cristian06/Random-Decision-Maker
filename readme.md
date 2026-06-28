# Random Decision Maker 🎲

A simple and intuitive web application designed to help users make quick decisions. Whether you're struggling to choose what to eat, what movie to watch, or which task to tackle first, this tool takes the hesitation out of decision-making by randomly selecting an option from your custom list.

## ✨ Features
* **Custom Input:** Users can input up to 7 distinct choices via a simple HTML form.
* **Randomized Selection:** Processes the submitted options and displays a single, unbiased random choice.
* **Minimalist UI:** Clean and straightforward interface built with HTML and CSS for a seamless user experience.
* **Dynamic Templating:** Utilizes Jinja2 templates via FastAPI to render choices and results dynamically on the frontend.

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS
* **Backend:** Python, FastAPI, Jinja2

## 🚀 How to Run Locally

Clone the repository:
   ```bash
   git clone [https://github.com/M-Cristian06/random-decision-maker.git](https://github.com/M-Cristian06/random-decision-maker.git) ```


Navigate to the project directory:


``` bash 
cd random-decision-maker```


Install the required dependencies:

```bash 
pip install fastapi uvicorn jinja2 ```


Start the local development server:

```bash 
uvicorn main:app --reload```

Open your browser and go to:

http://localhost:8000