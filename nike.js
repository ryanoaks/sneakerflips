const fetch = require("node-fetch");

async function getProductId() {
    let url = new URL ('https://api.nike.com/product_feed/threads/v2/')
    url.searchParams.append('count','14')
    url.searchParams.append('filter','marketplace(RU)')
    url.searchParams.append('filter','language(ru)')
    url.searchParams.append('filter','channelId(010794e5-35fe-4e32-aaff-cd2c74f89d61)')

    const resp = await fetch(url.href);
    const text = await resp.text();
    const json = await JSON.parse(text)

    if (resp.status === 200) {
        console.log('%c%s','color: white; background: green; font: 16px sans-serif; padding: 5px;',resp.status);
        console.log(json)
    } else {
        console.log('%c%s','color: white; background: red; font: 16px sans-serif; padding: 5px;',resp.status)
        throw new Error(`Error in fetch - ${resp.status}`)
    }
}

getProductId()