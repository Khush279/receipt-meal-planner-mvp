# Frontend - Receipt-to-Meal Planner MVP

React Native mobile application for the Receipt-to-Meal Planner MVP.

## 📱 Overview

This is the mobile frontend for the Receipt-to-Meal Planner application, built with React Native for cross-platform compatibility (iOS and Android). The app provides an intuitive interface for scanning receipts, managing pantry inventory, and viewing meal plans.

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── common/          # Generic components (Button, Input, Card, etc.)
│   │   ├── forms/           # Form-specific components
│   │   └── navigation/      # Navigation components
│   ├── screens/             # Screen components
│   │   ├── Scan/            # Receipt scanning functionality
│   │   ├── Pantry/          # Inventory management
│   │   ├── Plan/            # Meal planning and recipes
│   │   └── Analytics/       # Budget and waste analytics
│   ├── services/            # API and external service integrations
│   │   ├── api/             # Backend API client
│   │   ├── camera/          # Camera and image processing
│   │   └── storage/         # Local storage management
│   ├── styles/              # Figma design tokens integration
│   │   ├── tokens/          # Design tokens from Figma
│   │   ├── components/      # Component-specific styles
│   │   └── theme/           # App theme configuration
│   ├── navigation/          # React Navigation setup
│   ├── hooks/               # Custom React hooks
│   ├── utils/               # Utility functions
│   └── types/               # TypeScript type definitions
├── assets/                  # Images, icons, fonts
├── android/                 # Android-specific files
├── ios/                     # iOS-specific files
├── __tests__/               # Test files
├── package.json             # Dependencies and scripts
├── metro.config.js          # Metro bundler configuration
├── babel.config.js          # Babel configuration
├── react-native.config.js   # React Native CLI configuration
└── README.md               # This file
```

## 🎯 Key Features

### 📷 Scan Screen
- Camera integration for receipt capture
- Image preprocessing and optimization
- Real-time OCR feedback
- Manual item editing interface

### 🏪 Pantry Screen
- Live inventory display
- Add/edit/remove items
- Expiry date tracking
- Search and filter functionality

### 📋 Plan Screen
- AI-generated meal plans
- Recipe details and instructions
- Pantry utilization optimization
- Dietary preference settings

### 📊 Analytics Screen
- Spending dashboard
- Food waste tracking
- Budget vs actual analysis
- Shopping insights

## 🚀 Getting Started

### Prerequisites

- Node.js 16+
- React Native CLI
- Android Studio (for Android development)
- Xcode (for iOS development on macOS)
- CocoaPods (for iOS dependencies)

### Installation

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **iOS Setup** (macOS only)
   ```bash
   cd ios && pod install && cd ..
   ```

3. **Android Setup**
   - Ensure Android Studio and SDK are properly configured
   - Start an Android emulator or connect a device

4. **Start Metro bundler**
   ```bash
   npm start
   ```

5. **Run the application**
   ```bash
   # iOS
   npm run ios
   
   # Android
   npm run android
   ```

## 🎨 Design System Integration

### Figma Tokens

The app integrates with Figma design tokens for consistent styling:

- **Colors**: Primary, secondary, success, warning, error palettes
- **Typography**: Font families, sizes, weights, line heights
- **Spacing**: Margins, paddings, component spacing
- **Shadows**: Elevation and shadow styles
- **Border Radius**: Component corner radius values

### Token Usage

```typescript
import { tokens } from '@/styles/tokens';

const styles = StyleSheet.create({
  container: {
    backgroundColor: tokens.colors.background.primary,
    padding: tokens.spacing.md,
    borderRadius: tokens.borderRadius.md,
  },
  title: {
    fontFamily: tokens.typography.families.heading,
    fontSize: tokens.typography.sizes.xl,
    color: tokens.colors.text.primary,
  },
});
```

## 🔧 Development

### Available Scripts

```bash
# Start Metro bundler
npm start

# Run on iOS simulator
npm run ios

# Run on Android emulator/device
npm run android

# Run tests
npm test

# Run tests with coverage
npm run test:coverage

# Lint code
npm run lint

# Format code
npm run format

# Type check
npm run type-check

# Clean cache
npm run clean
```

### Code Style

- **ESLint**: Configured with React Native and TypeScript rules
- **Prettier**: Code formatting
- **TypeScript**: Strict type checking enabled
- **Husky**: Pre-commit hooks for linting and testing

### Testing

- **Jest**: Unit and integration testing
- **@testing-library/react-native**: Component testing utilities
- **Detox**: E2E testing framework

## 📚 Technical Stack

### Core Technologies
- **React Native**: 0.72+
- **TypeScript**: Type safety and better development experience
- **React Navigation**: Navigation framework
- **React Query**: Server state management
- **Zustand**: Local state management

### UI Components
- **React Native Elements**: Base component library
- **React Native Vector Icons**: Icon library
- **React Native Gesture Handler**: Touch and gesture handling
- **React Native Reanimated**: High-performance animations

### Camera & Image Processing
- **React Native Vision Camera**: Modern camera library
- **React Native Image Picker**: Gallery image selection
- **React Native Image Editor**: Basic image editing

### Storage & Networking
- **AsyncStorage**: Local key-value storage
- **MMKV**: High-performance local storage
- **Axios**: HTTP client
- **React Native MMKV**: Fast key-value storage

## 🔐 Environment Configuration

Create `.env` file in the frontend root:

```bash
# API Configuration
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30000

# Feature Flags
ENABLE_ANALYTICS=true
ENABLE_CRASH_REPORTING=true

# Third-party Services
SENTRY_DSN=your_sentry_dsn_here
MIXPANEL_TOKEN=your_mixpanel_token_here
```

## 📱 Platform-Specific Notes

### iOS
- Minimum iOS version: 12.0
- Camera permissions configured in Info.plist
- Photo library access permissions
- Push notification certificates required for production

### Android
- Minimum SDK version: 21 (Android 5.0)
- Camera and storage permissions in AndroidManifest.xml
- Proguard configuration for release builds
- Network security config for HTTP traffic

## 🧪 Testing Strategy

### Unit Tests
- Component rendering and behavior
- Utility function testing
- Custom hook testing
- Service layer testing

### Integration Tests
- API integration testing
- Navigation flow testing
- State management testing

### E2E Tests
- Critical user flows
- Receipt scanning workflow
- Meal planning process
- Analytics dashboard interaction

## 📈 Performance Optimization

- **Image optimization**: WebP support, lazy loading
- **Bundle splitting**: Code splitting for screens
- **Caching**: API response caching, image caching
- **Memory management**: Proper cleanup of listeners and subscriptions

## 🚀 Deployment

### Development Builds
```bash
# Generate Android APK
npm run build:android:debug

# Generate iOS build
npm run build:ios:debug
```

### Production Builds
```bash
# Android AAB for Play Store
npm run build:android:release

# iOS Archive for App Store
npm run build:ios:release
```

## 🤝 Contributing

1. Follow the established folder structure
2. Use TypeScript for all new components
3. Write tests for new features
4. Follow the design system guidelines
5. Update documentation for significant changes

## 📄 License

This project is licensed under the MIT License - see the main project LICENSE file for details.
