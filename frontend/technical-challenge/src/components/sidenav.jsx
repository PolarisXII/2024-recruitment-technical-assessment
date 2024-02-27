import React from "react";
import {
	BookOpenIcon,
	ShieldCheckIcon,
	BarsArrowDownIcon,
	BarsArrowUpIcon,
	UserCircleIcon,
	MoonIcon,
	ArrowRightEndOnRectangleIcon

  } from "@heroicons/react/24/outline";
import unilectives from '../assets/unilectives.svg';

export function SideBar() {

    return (
       <div className="flex flex-col static left-0 inset-y-0 bg-[#d9d9d9] w-[5%] h-screen text-black items-center justify-between">
        <div className="flex flex-col gap-7 left-0 top-0 justify-start">
            <button className="w-6 h-6 pt-8">
                <img src={unilectives}/>
            </button>

            <button className="w-6 h-6 pt-8">
                <BookOpenIcon></BookOpenIcon>
            </button>

            <button className="w-6 h-6 pt-8">
                <ShieldCheckIcon></ShieldCheckIcon>
            </button>
        </div>
       
        <div className="flex flex-col gap-7 left-0 top-0 justify-start">
            <button className="w-6 h-6 pt-8">
            <BarsArrowDownIcon></BarsArrowDownIcon>
            </button>

            <button className="w-6 h-6 pt-8">
                <UserCircleIcon></UserCircleIcon>
            </button>

            <button className="w-6 h-6 pt-8">
                <MoonIcon></MoonIcon>
            </button>

            <button className="w-6 h-6 pt-8">
                <ArrowRightEndOnRectangleIcon></ArrowRightEndOnRectangleIcon>
            </button>
        </div>
        
       </div>
    )
}