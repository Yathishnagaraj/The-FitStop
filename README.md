# TheFitStop - Sip. Snack. Power Up.

A simple health-focused beverage and snack shop website built with Flask and modern CSS.

## Project Structure

```
Web-code/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    └── style.css         # CSS styling
```

## Features

- **Homepage**: Hero section with call-to-action
- **About Section**: Information about TheFitStop
- **Contact Form**: User can send messages (printed to console)
- **Responsive Design**: Mobile-friendly layout

## Customization

### Adding Products
Edit the `products` list in `app.py` to add or modify products.

### Changing Colors
Modify the color variables in `static/style.css`:
- Primary color: `#667eea` (purple-blue)
- Secondary color: `#764ba2` (darker purple)
- Accent color: `#ff6b6b` (red)

### Styling
All CSS is in `static/style.css`. The design is fully responsive and mobile-friendly.

## Notes

- Contact messages are stored in memory (not persistent). For production, use a database.
- Email notifications are not implemented. You can add this using libraries like `Flask-Mail`.
- No authentication is implemented. For admin features, add user authentication.
- The site uses no JavaScript, making it simple and lightweight.

## Future Enhancements

- Database integration for persistent storage
- Email notifications on contact form submission
- Shopping cart functionality
- User authentication and accounts
- Payment integration
- Admin dashboard

## License

This project is created for TheFitStop. All rights reserved.
