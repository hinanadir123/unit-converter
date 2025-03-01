
#unit converter
#build a google converter app using python and streamlit

import streamlit as st
st.markdown(
    """
    <style>
    body {
       background-color: #1e1e2f
       color: white;
    }
    .stApp{
        background: linear-gradient(135deg,#bcbcbc, #cfe2f3);
        padding:30px;
        border-redius: 15px;
        box-shadow: 0px 10px,30px rgba(0,0,0,0,3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
    color:white;
    }
    .stButton>button{
        background-color: linear-gradient(45deg, #0b5394, #351c75);
        color:black;
        font-size:18px;
        paddingL 10px 20px;
        border-readius:10px;
        transition:0.3s;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
        }
    .stButton>button:hover{
        transform:scale(1.05);
        background: linear-gradient(45deg);
        color:black;
    }
    .result-box{
    border-radius: 10px;
    margin-top:20px;
    box-shadow: 0px 5px 15px rgba(0,201,255, 0.3);
    }
    .footer{
    text-align:center;
    margin-top: 50px;
    font-size:14px;
    color:black
    }    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1>  Unit Converter Using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write('Easily converter beteen different units of length, weight, and temperature.')


# side bar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["length", "weight", "temperature"])
value= st.number_input("Enter Value", value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "length":
    with col1:
        from_unit= st.selectbox("from", ["meters", "kilometers", "centimeters", "millimeters", "yards", "inches", "mile", "feet"])
    with col2:
        to_unit= st.selectbox("To", ["meters", "kilogram", "centimeters", "millimeters", "yards", "inches", "mile", "feet"])    
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("from", ["kilograms", "grams", "pounds", "milligrams","ounces"])    
    with col2:
        to_unit = st.selectbox("to", ["kilograms", "grams", "pounds", "milligrams","ounces"])    
elif conversion_type == "temperature":
    with col1:
        from_unit = st.selectbox("from", ["celcius", "Farnheight", "kelvin"])    
    with col2:   
        to_unit = st.selectbox("to", ["celcius", "fahrenheit", "kelvin"])


def length_converter(value, from_unit, to_unit):
    length_units ={
    'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters':1000,
    'miles': 0.000621371, 'yards': 1.09361,  'feet':3.28, 'inches': 39.37
    }
    return (value / length_units[from_unit])* length_units[to_unit]
    
def weight_converter(value, from_unit, to_unit):
    weight_units ={
        'kilograms':1 , 'grams': 1000, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.274
     }
    return (value / weight_units[from_unit] * weight_units[to_unit])

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celcius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else value +273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return(value -32) *5/9 if to_unit == "Celcius" else (value -32)* 5/9 + 273.15 if to_unit == "kelvin" else  value
    elif from_unit == "Kelivin":
        return value - 273.15 if to_unit =="Celcius" else (value-273.15) * 9/5 +32 if to_unit == "fahrenheit" else value
    return value

# button 
if st.button("Convert"):
    if conversion_type == "length":
       result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "weight":
       result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "temperature":
       result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)


st.markdown("<div class='footer'> Created by Hina Nadir Mughal </div>", unsafe_allow_html=True)










