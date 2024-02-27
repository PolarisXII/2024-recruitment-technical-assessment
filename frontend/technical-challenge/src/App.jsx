import unilectives from './assets/unilectives.svg';
import './App.css';

import {SideBar} from './components/sidenav'
import { TextHeader } from './components/text';
import { SearchBar } from './components/SearchBar';

export default function App() {
	const courses = require("./courses.json");
    console.log(courses)
  return (
    <div>
      {/* <div>
			<h1 className='text-normal left-5 top-5'>DevSoc presents: </h1>
			<h1 className='text-5xl font-bold text-theme-blue '> Unilectives </h1>
			<h2 className='text-normal font-bold'>Your one-stop stop for UNSW course and elective reviews</h2>
      </div> */}
	  <TextHeader/>
	  
	  <SideBar/>


	  
    </div>

  );
}

