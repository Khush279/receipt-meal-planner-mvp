# Receipt-to-Meal Planner MVP

## Overview

Receipt-to-Meal Planner MVP is an intelligent application that converts grocery receipts into personalized meal recommendations and weekly meal plans using AI-powered receipt scanning and nutritional analysis.

## 🎯 Product Vision

Help anyone turn grocery receipts into smart, budget-aware meal plans. The app understands what's in a user's pantry (from receipts, manual edits, and leftovers), plans meals that fit dietary preferences and expiry windows, and tracks spend vs. budget automatically.

## ✨ Key Features

### MVP (Version 1.0)
- **Receipt OCR + Parser**: Upload receipt photos and get structured JSON with items, quantities, prices, and store information
- **Smart Pantry Management**: Maintain live inventory with quantities, units, and best-before estimates
- **Meal Planning Engine**: Auto-generate 3/5/7-day vegetarian meal plans maximizing pantry utilization
- **Budget Tracking**: Monitor weekly spend, cost per meal, and budget variance
- **Manual Controls**: Add/edit items, consume/remove, adjust quantities, add leftovers

### Future Enhancements
- **v1.1**: Diet presets (vegan, pescetarian), household size support, protein targets
- **v1.2**: Barcode scanning, multi-store normalization, digital receipt imports
- **Beyond**: Cross-store price comparison, household sharing, macro tracking

## 🏗️ System Architecture

### Technology Stack
- **Frontend**: React Native or Flutter (mobile-first)
- **Backend**: NestJS/TypeScript or FastAPI/Python
- **Database**: PostgreSQL with pgvector for embeddings
- **Processing**: Redis job queue, S3/GCS object storage
- **AI/ML**: OCR (Tesseract + cloud fallback), LLM for extraction

### Core Components
1. **Receipt Processing Pipeline**: Image → OCR → Normalize → Extract → Canonicalize
2. **Inventory Management**: Real-time pantry tracking with expiry estimates
3. **Meal Planning Engine**: Recipe matching with pantry optimization
4. **Analytics Dashboard**: Spend tracking and waste reduction metrics

## 🎯 Target Users

- **Busy Students/Professionals**: Want cheap, fast meal plans with minimal manual tracking
- **Family Planners**: Multiple eaters, tight budgets, need weekly planning optimization
- **Quantified Savers**: Care about spend analytics, unit prices, store comparisons

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+ (for frontend)
- PostgreSQL 13+
- Redis 6+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Khush279/receipt-meal-planner-mvp.git
   cd receipt-meal-planner-mvp
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   cp .env.example .env
   # Configure your environment variables
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm start
   ```

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/receipt_planner

# Redis
REDIS_URL=redis://localhost:6379

# OCR Services
GOOGLE_VISION_API_KEY=your_key_here
AZURE_COGNITIVE_SERVICES_KEY=your_key_here

# OpenAI/LLM
OPENAI_API_KEY=your_key_here
```

## 📋 Project Structure

```
receipt-meal-planner-mvp/
├── backend/                 # API server
│   ├── src/
│   │   ├── auth/           # Authentication module
│   │   ├── receipts/       # Receipt processing
│   │   ├── inventory/      # Pantry management
│   │   ├── planning/       # Meal planning engine
│   │   └── analytics/      # Budget & waste tracking
│   ├── requirements.txt
│   └── README.md
├── frontend/               # Mobile/web app
│   ├── src/
│   │   ├── components/
│   │   ├── screens/
│   │   └── services/
│   ├── package.json
│   └── README.md
├── ml-pipeline/            # OCR & extraction services
├── docs/                   # Documentation
└── docker-compose.yml      # Development environment
```

## 🔧 Key Algorithms

### Receipt Parsing
- **OCR**: On-device Tesseract with cloud fallback (Google Vision/Azure)
- **LLM Extraction**: Structured JSON output with strict validation
- **Canonicalization**: Fuzzy matching against product database

### Meal Planning
- **Scoring Algorithm**: Prioritizes perishables by expiry, maximizes pantry coverage
- **Selection**: Greedy optimization with 1-day lookahead
- **Constraints**: Dietary preferences, budget limits, variety requirements

## 📊 Success Metrics

- **Activation**: 70% users complete first scan and save pantry (Week 1)
- **Utilization**: 50%+ of planned meals actually cooked
- **Parser Accuracy**: ≥93% line-item accuracy, <20% manual edit rate
- **Waste Reduction**: Perishables consumed before expiry
- **Budget Impact**: Users stay within weekly spend targets

## 🔒 Security & Privacy

- On-device OCR first to minimize PII exposure
- Receipt images encrypted at rest (SSE-S3)
- TLS for all API communications
- GDPR/CCPA compliant data export/deletion
- Rate limiting and authentication on all endpoints

## 🧪 Testing

### Run Tests
```bash
# Backend tests
cd backend && python -m pytest

# Frontend tests
cd frontend && npm test

# Integration tests
docker-compose -f docker-compose.test.yml up
```

### Test Coverage
- Unit tests for core algorithms (receipt parsing, meal planning)
- Integration tests for API endpoints
- E2E tests for critical user flows (scan → save → plan → cook)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint/Prettier for TypeScript/JavaScript
- Write tests for new features
- Update documentation for API changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Documentation**: Check the `/docs` folder for detailed guides
- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Join our GitHub Discussions for questions and ideas

## 🔄 Roadmap

### Phase 1 (MVP) - Q1 2025
- [x] Project setup and architecture
- [ ] Receipt OCR and parsing pipeline
- [ ] Basic pantry management
- [ ] Simple meal planning engine
- [ ] Budget tracking dashboard

### Phase 2 (v1.1) - Q2 2025
- [ ] Diet preference system
- [ ] Nutritional analysis
- [ ] Mobile app release
- [ ] Price history tracking

### Phase 3 (v1.2) - Q3 2025
- [ ] Barcode scanning
- [ ] Multi-store support
- [ ] Email receipt imports
- [ ] Advanced analytics

---

**Made with ❤️ for reducing food waste and saving money through smart meal planning.**
