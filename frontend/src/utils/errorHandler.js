export const getErrorMessage = (error) => {
  const detail = error.response?.data?.detail;

  if (Array.isArray(detail)) {
    return detail
      .map((err) => err.msg)
      .join(", ");
  }

  return detail || "Operation failed";
};