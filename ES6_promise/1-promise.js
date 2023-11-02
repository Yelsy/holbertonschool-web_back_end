function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    // Resolve the promise with a successful response
    if (success) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
        reject(new Error('The fake API is not working currently'));
    }
  });
}

export default getFullResponseFromAPI;
