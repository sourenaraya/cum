from cum.scrapers.dokireader import DokiReaderSeries, DokiReaderChapter
from cum.scrapers.dynastyscans import DynastyScansChapter, DynastyScansSeries
from cum.scrapers.madokami import MadokamiChapter, MadokamiSeries
from cum.scrapers.mangadex import MangadexSeries, MangadexChapter
from cum.scrapers.yuriism import YuriismChapter, YuriismSeries
from cum.scrapers.mangakakalot import MangaKakalotChapter, MangaKakalotSeries

series_scrapers = [
    DokiReaderSeries,
    DynastyScansSeries,
    MadokamiSeries,
    MangadexSeries,
    YuriismSeries,
    MangaKakalotSeries,
]
chapter_scrapers = [
    DokiReaderChapter,
    DynastyScansChapter,
    MadokamiChapter,
    MangadexChapter,
    YuriismChapter,
    MangaKakalotChapter,
]
