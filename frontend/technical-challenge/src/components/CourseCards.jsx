import React from "react";

export function CourseCards() {

    return (
        <div className="flex justify-center inset-0 bottom-0">
      <div>
        <div className="grid grid-cols-3 gap-20 mt-2">
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP1511</h1>
            <h1 className="pt-5">Programming Fundamentals</h1>
            </button>
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP1531</h1>
            <h1 className="pt-5">Software Engineering Fundamentals</h1>
            </button>
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP1521</h1>
            <h1 className="pt-5">Computer Systems Fundamentals</h1>
            </button>
        </div>
        <div className="grid grid-cols-3 gap-20 mt-2">
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP2521</h1>
            <h1 className="pt-5">Data Structure and Algorithms</h1>
            </button>
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP2511</h1>
            <h1 className="pt-5">Objected Oriented Programming</h1>
            </button>
            <button className="flex flex-col bg-white justify-start shadow-md rounded-lg p-4 w-80 h-60 text-neutral-700">
            <h1 className="text-2xl font-black">COMP3311</h1>
            <h1 className="pt-5">Database Systems</h1>
            </button>
            
        </div>
      </div>
    </div>
        
    )
}
