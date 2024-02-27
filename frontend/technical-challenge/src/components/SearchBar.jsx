import React from "react";
import {
	MagnifyingGlassIcon

} from "@heroicons/react/24/outline";

export function SearchBar() {
    return (
        <div className="mb-3 mt-7 ml-20 w-[80%]">
            <div className="relative mb-4 flex w-full items-stretch">
              <input
                  type="search"
                  className="relative block flex-auto rounded border border-solid border-neutral-300 border-theme-purple bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-theme-p outline-none transition duration-200 ease-in-out border-theme-purple border-2"
                  placeholder="Search for courses e.g: COMP1531"
                  aria-label="Search"
                  aria-describedby="button-addon2" />

              {/* <!--Search icon--> */}
              </div>
        </div>
        
    )
}