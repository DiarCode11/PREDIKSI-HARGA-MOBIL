import joblib
import pandas as pd


# data['owner'] = data['owner'].replace({'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5})
def encode_owner(owner : str): 
    if owner == 'First Owner': 
        return 1
    elif owner == 'Second Owner': 
        return 2
    elif owner == 'Third Owner': 
        return 3
    elif owner == 'Fourth & Above Owner': 
        return 4
    else: 
        return 5
    
def encode_transmission(transmission : str): 
    if transmission == 'Manual': 
        return 1
    elif transmission == 'Automatic': 
        return 2
    
def encode_seller_type(seller_type : str): 
    if seller_type == 'Individual': 
        return 1
    elif seller_type == 'Dealer': 
        return 2
    elif seller_type == 'Trustmark Dealer': 
        return 3
    
    
def set_merk(merk : str):
    # Membuat dictionary dengan nama merek mobil dan mengatur semuanya menjadi False
    merk_dict = {'Audi': False, 'BMW': False, 'Chevrolet': False,'Daewoo': False, 'Datsun': False, 'Fiat': False, 'Force': False,'Ford': False,'Honda': False, 'Hyundai': False, 'Isuzu': False, 'Jaguar': False,'Jeep': False, 'Kia': False, 'Land': False, 'MG': False, 'Mahindra': False, 'Maruti': False, 'Mercedes-Benz': False, 'Mitsubishi': False, 'Nissan': False, 'OpelCorsa': False, 'Renault': False, 'Skoda': False, 'Tata': False, 'Toyota': False, 'Volkswagen': False, 'Volvo': False}

    if merk == 'Audi': 
        merk_dict['Audi'] = True
    elif merk == 'BMW': 
        merk_dict['BMW'] = True
    elif merk == 'Chevrolet': 
        merk_dict['Chevrolet'] = True
    elif merk == 'Daewoo': 
        merk_dict['Daewoo'] = True
    elif merk == 'Datsun': 
        merk_dict['Datsun'] = True
    elif merk == 'Fiat': 
        merk_dict['Fiat'] = True
    elif merk == 'Force': 
        merk_dict['Force'] = True
    elif merk == 'Ford': 
        merk_dict['Ford'] = True
    elif merk == 'Honda': 
        merk_dict['Honda'] = True
    elif merk == 'Hyundai': 
        merk_dict['Hyundai'] = True
    elif merk == 'Isuzu': 
        merk_dict['Isuzu'] = True
    elif merk == 'Jaguar': 
        merk_dict['Jaguar'] = True
    elif merk == 'Jeep': 
        merk_dict['Jeep'] = True
    elif merk == 'Kia': 
        merk_dict['Kia'] = True
    elif merk == 'Land': 
        merk_dict['Land'] = True
    elif merk == 'MG': 
        merk_dict['MG'] = True
    elif merk == 'Mahindra': 
        merk_dict['Mahindra'] = True
    elif merk == 'Maruti': 
        merk_dict['Maruti'] = True
    elif merk == 'Mercedes-Benz': 
        merk_dict['Mercedes-Benz'] = True
    elif merk == 'Mitsubishi': 
        merk_dict['Mitsubishi'] = True
    elif merk == 'Nissan': 
        merk_dict['Nissan'] = True
    elif merk == 'OpelCorsa': 
        merk_dict['OpelCorsa'] = True
    elif merk == 'Renault': 
        merk_dict['Renault'] = True
    elif merk == 'Skoda': 
        merk_dict['Skoda'] = True
    elif merk == 'Tata': 
        merk_dict['Tata'] = True
    elif merk == 'Toyota': 
        merk_dict['Toyota'] = True
    elif merk == 'Volkswagen': 
        merk_dict['Volkswagen'] = True
    elif merk == 'Volvo': 
        merk_dict['Volvo'] = True
        
    return merk_dict

# 'fuel_Diesel', 'fuel_Electric', 'fuel_LPG', 'fuel_Petrol'
def set_fuel(fuel : str):
    fuel_dict = {'Diesel': False, 'Electric': False, 'CNG': False, 'Petrol': False}
    
    if fuel == 'Diesel': 
        fuel_dict['Diesel'] = True
    elif fuel == 'Electric': 
        fuel_dict['Electric'] = True
    elif fuel == 'CNG': 
        fuel_dict['CNG'] = True
    elif fuel == 'Petrol': 
        fuel_dict['Petrol'] = True
        
    return fuel_dict
    
def predict(merk : str, year : int, km_driven : int, fuel : str, seller_type : str, transmission : str, owner : str): 
    # Load model
    with open('random_forest_model.pkl', 'rb') as f:
        with open('scaler.pkl', 'rb') as g:
            model = joblib.load(f)
            # Load Scaler
            scaler = joblib.load(g)

            seller_type = encode_seller_type(seller_type)
            transmission = encode_transmission(transmission)
            owner = encode_owner(owner)
            merk = set_merk(merk)
            fuel = set_fuel(fuel)
            
            new_data = pd.DataFrame({
                'year': [year],
                'km_driven': [km_driven],
                'seller_type': [seller_type],
                'transmission': [transmission],
                'owner': [owner],
                'merk_Audi': [merk['Audi']],
                'merk_BMW': [merk['BMW']],
                'merk_Chevrolet': [merk['Chevrolet']],
                'merk_Daewoo': [merk['Daewoo']],
                'merk_Datsun': [merk['Datsun']],
                'merk_Fiat': [merk['Fiat']],
                'merk_Force': [merk['Force']],
                'merk_Ford': [merk['Ford']],
                'merk_Honda': [merk['Honda']],
                'merk_Hyundai': [merk['Hyundai']],
                'merk_Isuzu': [merk['Isuzu']],
                'merk_Jaguar': [merk['Jaguar']],
                'merk_Jeep': [merk['Jeep']],
                'merk_Kia': [merk['Kia']],
                'merk_Land': [merk['Land']],
                'merk_MG': [merk['MG']],
                'merk_Mahindra': [merk['Mahindra']],
                'merk_Maruti': [merk['Maruti']],
                'merk_Mercedes-Benz': [merk['Mercedes-Benz']],
                'merk_Mitsubishi': [merk['Mitsubishi']],
                'merk_Nissan': [merk['Nissan']],
                'merk_OpelCorsa': [merk['OpelCorsa']],
                'merk_Renault': [merk['Renault']],
                'merk_Skoda': [merk['Skoda']],
                'merk_Tata': [merk['Tata']],
                'merk_Toyota': [merk['Toyota']],
                'merk_Volkswagen': [merk['Volkswagen']],
                'merk_Volvo': [merk['Volvo']],
                'fuel_Diesel': [fuel['Diesel']],
                'fuel_Electric': [fuel['Electric']],
                'fuel_LPG': [fuel['LPG']],
                'fuel_Petrol': [fuel['Petrol']],
            })
            
            # Normalisasi fitur
            data_normalized = scaler.transform(new_data)

            # Prediksi
            prediction = model.predict(data_normalized)
            
            return prediction

list_of_merk = ['Audi', 'BMW', 'Chevrolet', 'Daewoo', 'Datsun', 'Fiat', 'Force','Ford','Honda', 'Hyundai', 'Isuzu', 'Jaguar','Jeep', 'Kia', 'Land', 'MG', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'OpelCorsa', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']
list_of_fuel = ['Diesel', 'Electric', 'CNG', 'Petrol']
list_of_seller_type = ['Individual', 'Dealer', 'Trustmark Dealer']
list_of_transmission = ['Manual', 'Automatic']
list_of_owner = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner']

if __name__ == "__main__":
    predict("Maruti", 2010, 80000, "Petrol", "Individual", "Manual", "First Owner")


