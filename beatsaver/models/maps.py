
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Type, Any, Optional

from .users import UserDetail

@dataclass(frozen=True)
class MapDetailMetadata:
  bpm: float
  duration: int
  songName: str
  songSubName: str
  songAuthorName: str
  levelAuthorName: str

  @classmethod
  def from_data(cls: Type[MapDetailMetadata], data: Any) -> MapDetailMetadata:
    return cls(
      bpm=data["bpm"],
      duration=data["duration"],
      songName=data["songName"],
      songSubName=data["songSubName"],
      songAuthorName=data["songAuthorName"],
      levelAuthorName=data["levelAuthorName"])

@dataclass(frozen=True)
class MapStats:
  plays: int
  downloads: int
  upvotes: int
  downvotes: int
  score: float

  @classmethod
  def from_data(cls: Type[MapStats], data: Any) -> MapStats:
    return cls(
      plays=data["plays"],
      downloads=data["downloads"],
      upvotes=data["upvotes"],
      downvotes=data["downvotes"],
      score=data["score"])

@dataclass(frozen=True)
class MapParitySummary:
  errors: int
  warns: int
  resets: int

  @classmethod
  def from_data(cls: Type[MapParitySummary], data: Any) -> MapParitySummary:
    return cls(
      errors=data["errors"],
      warns=data["warns"],
      resets=data["resets"])

@dataclass(frozen=True)
class MapDifficulty:
  njs: float
  offset: float
  notes: int
  bombs: int
  obstacles: int
  nps: float
  length: float
  characteristic: str
  difficulty: str
  events: int
  chroma: bool
  me: bool
  ne: bool
  cinema: bool
  seconds: float
  paritySummary: MapParitySummary
  stars: Optional[float]

  @classmethod
  def from_data(cls: Type[MapDifficulty], data: Any) -> MapDifficulty:
    return cls(
      njs=data["njs"],
      offset=data["offset"],
      notes=data["notes"],
      bombs=data["bombs"],
      obstacles=data["obstacles"],
      nps=data["nps"],
      length=data["length"],
      characteristic=data["characteristic"],
      difficulty=data["difficulty"],
      events=data["events"],
      chroma=data["chroma"],
      me=data["me"],
      ne=data["ne"],
      cinema=data["cinema"],
      seconds=data["seconds"],
      paritySummary=MapParitySummary.from_data(data["paritySummary"]),
      stars=data.get("stars"))

@dataclass(frozen=True)
class MapVersion:
  hash: str
  key: Optional[str]
  state: str
  createdAt: str
  sageScore: Optional[int]
  diffs: List[MapDifficulty]
  downloadURL: str
  coverURL: str
  previewURL: str

  @classmethod
  def from_data(cls: Type[MapVersion], data: Any) -> MapVersion:
    diffs = []
    for diff_data in data["diffs"]:
        diffs.append(MapDifficulty.from_data(diff_data))

    return cls(
      hash=data["hash"],
      # Old maps include the key, new ones don't
      # Because what's consistency? :tf:
      key=data.get("key"),
      state=data["state"],
      createdAt=data["createdAt"],
      # Same story as the key above
      sageScore=data.get("sageScore"),
      diffs=diffs,
      downloadURL=data["downloadURL"],
      coverURL=data["coverURL"],
      previewURL=data["previewURL"])

@dataclass(frozen=True)
class MapDetail:
  id: str
  name: str
  description: str
  uploader: UserDetail
  metadata: MapDetailMetadata
  stats: MapStats
  uploaded: str
  automapper: bool
  ranked: bool
  qualified: bool
  versions: List[MapVersion]

  @classmethod
  def from_data(cls: Type[MapDetail], data: Any) -> MapDetail:

    versions = []
    for version_data in data["versions"]:
        versions.append(MapVersion.from_data(version_data))

    return cls(
      id=data["id"],
      name=data["name"],
      description=data["description"],
      uploader=UserDetail.from_data(data["uploader"]),
      metadata=MapDetailMetadata.from_data(data["metadata"]),
      stats=MapStats.from_data(data["stats"]),
      uploaded=data["uploaded"],
      automapper=data["automapper"],
      ranked=data["ranked"],
      qualified=data["qualified"],
      versions=versions)
