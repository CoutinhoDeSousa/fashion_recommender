from src.data_pipeline.preprocess import preprocess_image

def test_preprocess_image():
    resize_dimension = (28,28)
    processed = preprocess_image("data/raw/example.jpg", resize_dimension)
    assert processed.shape == resize_dimension