# DeepFake Image Detector (Real vs Fake)

This project provides a simple desktop GUI application to detect whether an input image is **Real** or **Fake (DeepFake)** using a trained **TensorFlow/Keras** model.

## What it does
- Loads a trained Keras model (`bestmodel.keras`).
- Lets the user **upload an image** via a Tkinter interface.
- Preprocesses the image (resize + normalization).
- Runs inference and displays the result:
  - **“The image is Real.”** if the prediction is `> 0.5`
  - **“The image is Fake.”** otherwise

## How to run
1. Ensure you have the required Python dependencies installed (see **Requirements**).
2. Open/run the GUI script:
   - `DEEPFAKE IMAGE DETECTOR/DFID.py`

### Run command (from the project root)
```bash
python "DEEPFAKE IMAGE DETECTOR/DFID.py"
```

## Important note: model path
Inside `DEEPFAKE IMAGE DETECTOR/DFID.py`, the model path is currently **hardcoded**:

```python
MODEL_PATH = r"C:\\Users\\Admin\\Desktop\\bestmodel\\bestmodel.keras"
```

You must update `MODEL_PATH` to point to your local location of `bestmodel.keras`.

## GUI usage
1. Click **Choose File**.
2. Select a `.png`, `.jpg`, or `.jpeg` image.
3. Click **Detect DeepFake**.
4. The app will display the classification result in the output area.

## How inference works (high level)
- The input image is resized to **128×128**.
- Converted to a numpy array.
- Normalized by dividing by **255.0**.
- Added a batch dimension.
- `model.predict()` is used to obtain a single prediction score.
- A threshold of **0.5** determines the final label.

## Project structure
- `DEEPFAKE IMAGE DETECTOR/DFID.py` — Tkinter GUI + deepfake detection logic
- `DEEPFAKE IMAGE DETECTOR/bestmodel.keras` — trained Keras model (ensure `MODEL_PATH` points to this)
- `DEEPFAKE IMAGE DETECTOR/ProjectPrototype.ipynb` — notebook used during development/prototyping
- `DEEPFAKE IMAGE DETECTOR/Screenshot 2024-12-12 031104.png` — UI screenshot

## Requirements
The project uses:
- Python
- TensorFlow / Keras (`tensorflow.keras`)
- NumPy
- Tkinter (usually included with Python on Windows)

You can install TensorFlow and NumPy with:
```bash
pip install tensorflow numpy
```

## Troubleshooting
- **Model not found / load_model error**: update `MODEL_PATH` in `DFID.py`.
- **Missing tkinter**: install/repair your Python installation (Tkinter support is required for the GUI).
- **Input shape mismatch**: if you retrain the model with a different input size, also update the resize target in `DFID.py`.

## Notes
This README is based on the current GUI implementation in `DEEPFAKE IMAGE DETECTOR/DFID.py`.

