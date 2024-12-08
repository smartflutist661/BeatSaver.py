from __future__ import annotations

from dataclasses import dataclass
from typing import Type, Any, Optional

@dataclass(frozen=True)
class UserDiffStats:
  easy: int
  expert: int
  expertPlus: int
  hard: int
  normal: int
  total: int

  @classmethod
  def from_data(cls: Type[UserDiffStats], data: Any) -> UserDiffStats:
    return cls(
      easy=data["easy"],
      expert=data["expert"],
      expertPlus=data["expertPlus"],
      hard=data["hard"],
      normal=data["normal"],
      total=data["total"])

@dataclass(frozen=True)
class UserStats:
  totalUpvotes: int
  totalDownvotes: int
  totalMaps: int
  rankedMaps: int
  avgBpm: float
  avgDuration: float
  avgScore: float
  firstUpload: str
  lastUpload: str
  diffStats: UserDiffStats

  @classmethod
  def from_data(cls: Type[UserStats], data: Any) -> UserStats:
    return cls(
      totalUpvotes=data["totalUpvotes"],
      totalDownvotes=data["totalDownvotes"],
      totalMaps=data["totalMaps"],
      rankedMaps=data["rankedMaps"],
      avgBpm=data["avgBpm"],
      avgDuration=data["avgDuration"],
      avgScore=data["avgScore"],
      firstUpload=data["firstUpload"],
      lastUpload=data["lastUpload"],
      diffStats=UserDiffStats.from_data(data["diffStats"]))

@dataclass(frozen=True)
class UserDetail:
  id: str
  name: str
  hash: Optional[str]
  avatar: str
  stats: Optional[UserStats]

  @classmethod
  def from_data(cls: Type[UserDetail], data: Any) -> UserDetail:

    user_stats_data = data.get("stats")
    user_stats = None
    if user_stats_data:
      user_stats = UserStats.from_data(user_stats_data)

    return cls(
      id=data["id"],
      name=data["name"],
      hash=data.get("hash"),
      avatar=data["avatar"],
      stats=user_stats)
