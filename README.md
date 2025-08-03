
# 🧠 Brain Tumor Detection Web Application

A full-stack deep learning web application for detecting brain tumors from MRI images. Built with Django and integrated with a Convolutional Neural Network (CNN) model trained using TensorFlow/Keras. This system enables users to register, upload MRI scans, and receive real-time diagnostic predictions through a simple web interface.

---

## Features

- User registration and login system
- MRI image upload form with secure file handling
- Real-time brain tumor prediction using a CNN model
- Prediction history tracking per user
- Clean and responsive frontend
- Admin panel to manage users and test results

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS (Django Templates)
- **Backend**: Django (Python)
- **Machine Learning**: Keras, TensorFlow, OpenCV, NumPy
- **Database**: SQLite (Django default)
- **Image Processing**: Pillow, OpenCV

---

## Model

- Pretrained CNN model (`BrainTumor10Epochs.h5`)
- Input: MRI Image (64x64 pixels)
- Output: Binary classification (Tumor / No Tumor)
- Accuracy: ~93% on validation set

---

## 📁 Project Structure

- `models.py`: Defines user profile and test result models
- `forms.py`: Image upload form
- `views.py`: Handles routing, image prediction logic, user authentication
- `urls.py`: URL patterns for all pages
- `templates/`: Contains HTML pages like home, login, profile, history, etc.
- `static/`: For static CSS/JS files
- `media/`: Stores uploaded MRI images

---

## Sample Workflow

1. User registers and logs in
2. Uploads an MRI scan via the "Model" page
3. The app runs prediction and displays the result (Tumor / No Tumor)
4. The result is saved with the date and image in the user's history
5. Users can view past results anytime

---

## ⚠️ Challenges Solved

- Handled class imbalance and image noise in MRI data
- Optimized model for real-time inference
- Implemented secure user management and session handling

---

## How to Run Locally

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `BrainTumor10Epochs.h5` in the project root
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`

---

## 👨‍⚕️ Admin Access (Optional)

To access Django admin:
```bash
python manage.py createsuperuser
```

Then visit `/admin` and log in.

---

## 📌 Note

This application is intended for **educational and experimental purposes** only. It is **not a certified medical tool** and should not be used for clinical diagnosis.
