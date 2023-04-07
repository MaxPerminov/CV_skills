export const fd = async function getData(url, arr, method="GET") {
  const data = await fetch(url,{
    method:method
  })
  const parsedData = await data.json()
  if (Array.isArray(parsedData)) {arr.push(...parsedData)
    return arr}
  return parsedData
}
