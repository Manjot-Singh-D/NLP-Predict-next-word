// import logo from './logo.svg';
import {React,useEffect,useState} from "react";
import './App.css';
import axios from "axios";

function App() {
  const [text,setText]=useState("");
  const [order,setOrder]=useState(1);
  const [pred,setPred]=useState("");
  const [appear,setAppear]=useState(false);
  useEffect(()=>{
    // console.log("Order Val Changed!! : ",order);
  },[order])
  const onTextChange=(event)=>{
    const { name, value } = event.target;
    // console.log("value : ",value);
    setText((prevText) => {
      return {
        ...prevText,
        [name]: value,
      };
    });
    setAppear(false);
    // console.log("Text is : ",text[name]?.split(" "));
    // console.log(text[name]?.split(" ").length);
    // console.log("Size : ",text[name]?.split(" ").length);
    if(value[value.length-1]===" " && text[name]?.split(" ").length>=order){
      // console.log("Checking Response!!!");
      let sendData={order:order,text:text[name]};
      axios.post('http://localhost:5000/api/getWord',sendData).then((res)=>{
        // console.log(res);
        setPred(res.data[0].resp);
        setAppear(true);
      }).catch((err)=>{
        console.log("Error : ",err);
      })
    }
  }
  return (
    <div className="App">
    <h1 style={{textAlign:"center",margin:"1rem 0rem",color:"#ffffff"}}>Predict the next Word!!</h1>
    <div style={{display:"flex",justifyContent:"center",alignItems:"center",flexDirection:"row"}}>
      <div style={{outline:"none",margin:"10px",padding:"1rem", border:"1px solid white",width:"max-content",cursor:"pointer",background:order===1?"#f2aa4cff":"#ffffff"}} onClick={()=>setOrder(1)}>Order 1</div>
      <div style={{outline:"none",margin:"10px",padding:"1rem", border:"1px solid white",width:"max-content",cursor:"pointer",background:order===2?"#f2aa4cff":"#ffffff"}} onClick={()=>setOrder(2)}>Order 2</div>
      <div style={{outline:"none",margin:"10px",padding:"1rem", border:"1px solid white",width:"max-content",cursor:"pointer",background:order===3?"#f2aa4cff":"#ffffff"}} onClick={()=>setOrder(3)}>Order 3</div>
    </div>
      
      <div style={{border:"0.5px solid white", padding:"1rem",width:"500px",margin:"3rem auto"}}>
        <input type={"text"} name="text" onChange={onTextChange} style={{padding:"0.5rem",background:"#ffffff",color:"#000000",marginTop:"2rem",outline:"none",border:"none",width:"300px"}}/>
        <div style={{color:"#ffffff",marginTop:"1rem"}}>Predicted text : <span style={{color:"#ffffff",fontWeight:"900",fontStyle:"italic"}}>{pred?pred:appear?"No suggestion":"...."}</span></div>
        
      </div>
    </div>
  );
}

export default App;
