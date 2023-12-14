import { combineReducers } from "redux";
import HomePageReducer from "./HomePageReducer";

const createRootReducer = (history) =>
    combineReducers({
        homePage: HomePageReducer
    })

export default createRootReducer