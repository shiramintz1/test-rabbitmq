import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface User {
  userName: string;
  password: string;
  email: string;
}

interface UserState {
  currentUser: User | null;
}

const initialState: UserState = {
  currentUser: null,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setCurrentUser: (state, action: PayloadAction<User>) => {
      state.currentUser = action.payload;
    },
    clearCurrentUser: (state) => {
      state.currentUser = null;
    },
    updateCurrentUser: (state, action: PayloadAction<Partial<User>>) => {
      if (state.currentUser) {
        state.currentUser = {
          ...state.currentUser,
          ...action.payload,
        };
      }
    },
  },
});

export const {
  setCurrentUser,
  clearCurrentUser,
  updateCurrentUser,
} = userSlice.actions;

export default userSlice.reducer;
