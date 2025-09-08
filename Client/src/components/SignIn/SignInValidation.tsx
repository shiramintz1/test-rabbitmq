export interface UserDetails {
  userName: string;
  fullName: string;
  email: string;
  password: string;
}

export interface ValidationErrors {
  userName?: string;
  fullName?: string;
  email?: string;
  password?: string;
}

export const validateUserDetails = (data: UserDetails): ValidationErrors => {
  const errors: ValidationErrors = {};

  const usernameRegex = /^[a-zA-Z0-9._]{6,20}$/;
  if (!data.userName) {
    errors.userName = 'שדה חובה';
  } else if (!usernameRegex.test(data.userName)) {
    errors.userName = 'Username לא תקין: 6-20 תווים, אותיות באנגלית, ספרות, _ או . בלבד';
  }

  if (!data.fullName) {
    errors.fullName = 'שדה חובה';
  } else if (data.fullName.length > 30) {
    errors.fullName = 'השם לא יכול להיות ארוך מ-30 תווים';
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!data.email) {
    errors.email = 'שדה חובה';
  } else if (!emailRegex.test(data.email)) {
    errors.email = 'אימייל לא תקין';
  }

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

  if (!data.password) {
    errors.password = 'שדה חובה';
  } else if (!passwordRegex.test(data.password)) {
    errors.password = 'סיסמה חלשה: חייבת לכלול שמונה תווים, אותיות גדולות, קטנות, מספר ותו מיוחד';
  }

  return errors;
};
