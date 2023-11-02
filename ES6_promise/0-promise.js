function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (true) {
      resolve();
    }
    else {
      reject(new Error('error'));
    }
  });
}

export default getResponseFromAPI;
