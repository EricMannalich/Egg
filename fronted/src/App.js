import './App.css';
import { useEffect, useState } from "react";
import axios from "axios";
import PostList from './components/post-list';

const url = "http://127.0.0.1:8000/usuario/usuario/"

function App() {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    fetchData()
  }, []);

  const fetchData = () => {
    axios.get(url).then(res => {
      //console.log(res)
      //console.log(res.data)
      setPosts(res.data)
    })
      .catch((err) => console.log(err))
  }
  return (
    <div className="App">
      <div>Hello word</div>
      <hr />
      <PostList data={posts} />
    </div>
  );
}

export default App;
