// Deep Equality Check Function
export function deepEquals(obj1, obj2) {
    // Check for null and undefined
    if (obj1 === null || obj1 === undefined || obj2 === null || obj2 === undefined) {
      return obj1 === obj2;
    }
  
    // Check for primitive types
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object') {
      return obj1 === obj2;
    }
  
    // Check for Array vs Object
    if (Array.isArray(obj1) !== Array.isArray(obj2)) {
      return false;
    }
  
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);
  
    // Check if both objects have the same number of keys
    if (keys1.length !== keys2.length) {
      return false;
    }
  
    // Recursive check
    for (const key of keys1) {
      if (!keys2.includes(key) || !deepEquals(obj1[key], obj2[key])) {
        return false;
      }
    }
  
    return true;
  }
  