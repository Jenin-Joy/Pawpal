# PawPal - Pet Social Network Platform

## Overview
PawPal is a social networking platform designed specifically for pet owners and their beloved companions. The platform allows pets (through their owners) to connect, share moments, find lost pets, and interact with pet-related businesses.

## Features

### For Pet Owners
- **Profile Management**: Create and manage pet profiles with photos and details
- **Social Feed**: Share posts, photos, and updates about your pets
- **Groups**: Join and participate in pet-related groups
- **Lost Pet System**: Report and help find lost pets
- **Complaint System**: Submit and track pet-related complaints
- **Shop Directory**: Browse and connect with pet-related businesses
- **Notifications**: Stay updated with activities and interactions

### For Shops
- **Business Profile**: Create and manage shop profiles
- **Product/Service Listing**: Showcase pet-related products and services
- **Customer Interaction**: Connect with pet owners directly

## Technical Stack

### Frontend
- HTML5/CSS3
- JavaScript
- Bootstrap 5.0.0
- Font Awesome Icons
- Various JS libraries (jQuery, Chart.js, etc.)

### Backend
- Django (Python Web Framework)
- SQLite Database

### Admin Dashboard
- Star Admin 2 Template
- TinyMCE 5.6.2 for rich text editing
- Various data visualization tools (Chartist.js, Google Charts)

## Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Create and activate virtual environment
```bash
python -m venv MainEnv
source MainEnv/bin/activate  # For Unix/macOS
MainEnv\Scripts\activate     # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
python manage.py runserver
```

## Project Structure
```
PawPal/
├── Guest/           # Guest user management
├── Pet/             # Pet profile and features
├── Templates/       # HTML templates
│   ├── Guest/
│   └── Pet/
└── static/         # Static files
    ├── Admin/      # Admin dashboard assets
    └── Main/       # Main site assets
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- Star Admin 2 for admin dashboard template
- TinyMCE for rich text editing capabilities
- Bootstrap team for frontend framework
- All contributors who have helped shape PawPal

## Contact
Project Link: [repository-url]