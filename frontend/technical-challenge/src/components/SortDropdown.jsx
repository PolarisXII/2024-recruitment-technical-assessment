import React from "react";
import { Dropdown, DropdownButton } from "react-bootstrap";
 
export function SortDrop() {
    return (
        
        <DropdownButton title="Sort By" className=" mb-3 mt-5 ml-20 w-[20%] text-neutral-600 text-left justify-items-start relative block flex-auto rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] outline-none transition duration-200 ease-in-out border-2">
            
                <Dropdown.Item>name</Dropdown.Item>
                <Dropdown.Item>rating</Dropdown.Item>
                
        </DropdownButton>
        
    )
}