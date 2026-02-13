# Contributing to NASDAQ Wishlist Tracker

Thank you for considering contributing! This document outlines the process for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, browser)

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature already exists
- Open an issue with detailed description
- Explain the use case
- Consider implementation complexity

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   - Ensure app runs without errors
   - Test with various ticker symbols
   - Check UI on different screen sizes

5. **Commit your changes**
   ```bash
   git commit -m "Add: descriptive commit message"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Wait for review

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Keep functions focused and small
- Add docstrings for functions
- Comment complex logic

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/nasdaq-wishlist-tracker.git
cd nasdaq-wishlist-tracker
pip install -r requirements.txt
python app.py
```

## Testing

Currently, this project uses manual testing:
1. Run the app
2. Add various ticker symbols
3. Verify all indicators calculate correctly
4. Test error handling with invalid tickers
5. Check UI responsiveness

## Areas for Contribution

### High Priority
- Add unit tests (pytest)
- Implement CSV import/export
- Add sorting functionality
- Improve error messages

### Medium Priority
- Add more technical indicators
- Implement caching for API calls
- Add dark mode
- Mobile app wrapper

### Low Priority
- Add historical backtesting
- Email/SMS alerts
- Portfolio tracking
- Multiple watchlists

## Questions?

Feel free to open an issue for any questions!

Thank you for contributing! 🙏
