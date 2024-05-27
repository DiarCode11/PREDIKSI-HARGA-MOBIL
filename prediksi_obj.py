import os
import pickle

class PrediksiHarga:
    model = None

    @classmethod
    def load_model(cls):
        if cls.model is None:
            with open('car_price_model.pkl', 'rb') as f:
                cls.model = pickle.load(f)

    def __init__(self, message_id: int, user_id: int):
        self.merk: str | None = None
        self.year: int | None = None
        self.km_driven: int | None = None
        self.fuel: str | None = None
        self.seller_type: str | None = None
        self.transmission: str | None = None
        self.owner: str | None = None
        self.message_id = message_id
        self.user_id = user_id
        self.load_model()
        
    def save(self):
        # create folder
        if not os.path.exists('saved_objects'):
            os.makedirs('saved_objects')
        with open(f'saved_objects/{self.message_id}.pickle', 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load(message_id: int):
        with open(f'saved_objects/{message_id}.pickle', 'rb') as f:
            return pickle.load(f)
        
    def delete(self):
        os.remove(f'saved_objects/{self.message_id}.pickle')
    
    def set_merk(self, merk: str):
        self.merk = merk
    
    def set_fuel(self, fuel: str):
        self.fuel = fuel
        
    def set_year(self, year: int):
        self.year = year
    
    def set_km_driven(self, km_driven: int):
        self.km_driven = km_driven
    
    def set_seller_type(self, seller_type: str):
        self.seller_type = seller_type
    
    def set_transmission(self, transmission: str):
        self.transmission = transmission
    
    def set_owner(self, owner: str):
        self.owner = owner
    
    def prediksi_harga(self):
        features = [self.merk, self.year, self.km_driven, self.fuel, self.seller_type, self.transmission, self.owner]
        # Preprocess features if necessary
        # Example: features = preprocess(features)

        if None in features:
            raise ValueError("All features must be set before making a prediction.")
        
        prediction = self.model.predict([features])
        return prediction[0]
