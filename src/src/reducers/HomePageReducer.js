import initialState from "../components/initialState";
import { SET_VISIBLE } from "../constants/HomePage";


export default function HomePageReducer(
    state = initialState.homePage,
    action
) {
    let newState = JSON.parse(JSON.stringify(state))

    switch (action.type) {
        case SET_VISIBLE:
            newState.homePage.visible = action.visible
            return newState;
        default:
            return state;
    }
}