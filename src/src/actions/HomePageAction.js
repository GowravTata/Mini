import { SET_VISIBLE } from "../constants/HomePage";



const setAddVisible = (addVisible, dispatch) => {
    dispatch({
        type: SET_VISIBLE,
        payload: {
            visible: addVisible
        }
    })
}

const HomePageAction = {
    setAddVisible
}

export default HomePageAction