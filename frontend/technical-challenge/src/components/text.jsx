import React from "react";
import { SearchBar } from "./SearchBar";
import { SortDrop } from "./SortDropdown";
import Dropdown from 'react-bootstrap';
import { CourseCards } from "./CourseCards";
export function TextHeader() {
    return (
        <div className="mx-20 absolute inset-x-0 top-0 justify-center">
            <p className="font-sans ml-20 mt-6">DevSoc presents</p>
            <h1 className="font-sans font-black text-theme-blue text-5xl mt-5 ml-20">unilectives</h1>
            <h2 className="font-sans font-extrabold text-normal mt-5 ml-20">Your one-stop shop for UNSW courses and elective reviews.</h2>
            <SearchBar className="mt-10"></SearchBar>
            <SortDrop className="mt-10 w-50%"></SortDrop>
            <CourseCards></CourseCards>
        </div>
    )
}