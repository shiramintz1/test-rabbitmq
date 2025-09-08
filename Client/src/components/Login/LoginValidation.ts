export interface UserDetails {
  userName: string;
  password: string;
  email?: string;
}

export interface ValidationErrors {
  userName?: string;
  password?: string;
  email?: string;
}

export const validateUserDetails = (data: UserDetails): ValidationErrors => {
  const errors: ValidationErrors = {};

  if (!data.userName) {
    errors.userName = 'required field';
  } else if (data.userName.length > 30) {
    errors.userName = 'The name cannot be longer than 30 characters';
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!data.email) {
    errors.email = 'required field';
  } else if (!emailRegex.test(data.email)) {
    errors.email = 'Invalid email';
  }

  const passwordRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

  if (!data.password) {
    errors.password = 'required field';
  } else if (!passwordRegex.test(data.password)) {
    errors.password =
      'Weak password: must contain at least 8 characters, uppercase, lowercase, number, and special character';
  }

  return errors;
};


