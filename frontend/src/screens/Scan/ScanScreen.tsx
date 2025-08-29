import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import Icon from 'react-native-vector-icons/MaterialIcons';

// TODO: Import camera and image picker services
// import { CameraService } from '@/services/camera';
// import { ImagePickerService } from '@/services/camera';

interface ScanScreenProps {
  navigation: any; // TODO: Replace with proper navigation type
}

const ScanScreen: React.FC<ScanScreenProps> = ({ navigation }) => {
  const [isProcessing, setIsProcessing] = useState(false);

  const handleCameraCapture = async () => {
    try {
      setIsProcessing(true);
      // TODO: Implement camera capture logic
      // const result = await CameraService.captureReceipt();
      // Process the captured image
      console.log('Camera capture initiated');
      Alert.alert('Feature Coming Soon', 'Camera capture will be implemented');
    } catch (error) {
      console.error('Camera capture error:', error);
      Alert.alert('Error', 'Failed to capture image');
    } finally {
      setIsProcessing(false);
    }
  };

  const handleGalleryPick = async () => {
    try {
      setIsProcessing(true);
      // TODO: Implement gallery picker logic
      // const result = await ImagePickerService.selectFromGallery();
      // Process the selected image
      console.log('Gallery picker initiated');
      Alert.alert('Feature Coming Soon', 'Gallery picker will be implemented');
    } catch (error) {
      console.error('Gallery picker error:', error);
      Alert.alert('Error', 'Failed to select image');
    } finally {
      setIsProcessing(false);
    }
  };

  const navigateToPantry = () => {
    navigation.navigate('Pantry');
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Scan Receipt</Text>
        <Text style={styles.subtitle}>
          Take a photo or select an existing receipt to add items to your pantry
        </Text>
      </View>

      <View style={styles.content}>
        <View style={styles.scanOptions}>
          <TouchableOpacity
            style={[styles.optionButton, styles.cameraButton]}
            onPress={handleCameraCapture}
            disabled={isProcessing}
          >
            <Icon name="camera-alt" size={48} color="#FFFFFF" />
            <Text style={styles.optionButtonText}>Take Photo</Text>
            <Text style={styles.optionButtonSubtext}>
              Capture receipt with camera
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.optionButton, styles.galleryButton]}
            onPress={handleGalleryPick}
            disabled={isProcessing}
          >
            <Icon name="photo-library" size={48} color="#FFFFFF" />
            <Text style={styles.optionButtonText}>Choose from Gallery</Text>
            <Text style={styles.optionButtonSubtext}>
              Select existing receipt photo
            </Text>
          </TouchableOpacity>
        </View>

        {isProcessing && (
          <View style={styles.processingContainer}>
            <Text style={styles.processingText}>Processing...</Text>
          </View>
        )}
      </View>

      <View style={styles.footer}>
        <TouchableOpacity style={styles.pantryButton} onPress={navigateToPantry}>
          <Icon name="inventory" size={24} color="#007AFF" />
          <Text style={styles.pantryButtonText}>View Pantry</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8F9FA',
  },
  header: {
    paddingHorizontal: 24,
    paddingVertical: 32,
    alignItems: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#1A1A1A',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#6B7280',
    textAlign: 'center',
    lineHeight: 24,
  },
  content: {
    flex: 1,
    paddingHorizontal: 24,
    justifyContent: 'center',
  },
  scanOptions: {
    gap: 16,
  },
  optionButton: {
    backgroundColor: '#007AFF',
    borderRadius: 16,
    padding: 32,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 4,
  },
  cameraButton: {
    backgroundColor: '#007AFF',
  },
  galleryButton: {
    backgroundColor: '#34C759',
  },
  optionButtonText: {
    fontSize: 20,
    fontWeight: '600',
    color: '#FFFFFF',
    marginTop: 12,
    marginBottom: 4,
  },
  optionButtonSubtext: {
    fontSize: 14,
    color: '#E8F4FF',
    textAlign: 'center',
  },
  processingContainer: {
    marginTop: 32,
    alignItems: 'center',
  },
  processingText: {
    fontSize: 16,
    color: '#6B7280',
    fontWeight: '500',
  },
  footer: {
    paddingHorizontal: 24,
    paddingBottom: 32,
    alignItems: 'center',
  },
  pantryButton: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#007AFF',
    gap: 8,
  },
  pantryButtonText: {
    fontSize: 16,
    color: '#007AFF',
    fontWeight: '500',
  },
});

export default ScanScreen;
