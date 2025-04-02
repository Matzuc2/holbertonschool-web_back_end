

export default function loadBalancer(chinaDownload, USDownload) {
    const prom1 = Promise.race([chinaDownload, USDownload])
    return prom1
}