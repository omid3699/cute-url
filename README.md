
# Cute URL

**Cute URL** is a fun and elegant URL shortener built with Django and HTMX. It makes shortening URLs not just simple but downright adorable! Whether you're sharing links with friends or streamlining your digital content, Cute URL is here to bring a smile to your face and efficiency to your workflow.

## Features

- **Instant URL Shortening:** Convert long, messy URLs into compact, shareable links with a single click.

- **Real Time Click Tracking:** Get click count of urls real time with short polling.

- **Custom Aliases:** Personalize your short links with custom aliases.
- **Dynamic Interactions:** Enjoy seamless, modern user interactions powered by HTMX, with no page reloads.
- **Responsive Design:** Look cute and function smoothly on both desktop and mobile devices.
- **Built with Django:** Leverage the robustness and scalability of Django for your URL shortening needs.

## Getting Started

Follow these steps to get your own instance of Cute URL up and running locally.

### Prerequisites

- Python 3.9 or higher
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/omid3699/cute-url.git
   cd cute-url
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**

   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start shortening URLs!

## Usage

1. **Shorten a URL:** Enter your long URL into the form. Optionally, add a custom alias for your short URL.
2. **Get Your Short Link:** Once processed, your new short URL will be displayed for easy sharing.
3. **Experience Dynamic Updates:** Thanks to HTMX, all interactions are smooth and instantaneous without full page reloads.

## Technologies Used

- **Django:** Robust backend framework.
- **HTMX:** For modern, dynamic frontend interactions.
- **SQLite:** Default database for development (easily replaceable with other databases in production).
- **Tailwindcss:** For Cute style for frontend.

## Contributing

We love contributions that help make Cute URL even cuter! If you'd like to contribute, please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -am 'Add some cool feature'
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django HTMX and tailwindcss:** Thanks to the developers and communities that built these amazing tools.

---

Enjoy shortening URLs the cute way with **Cute URL**! If you have any suggestions or improvements, feel free to reach out or contribute. Happy coding!
