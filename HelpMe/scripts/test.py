#!/user/bin/env cmsRun

import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

process.load("HelpMe.HelpMe.ZH124_cff")

process.genParticlesForFilter = cms.EDProducer("GenParticleProducer",
  saveBarCodes = cms.untracked.bool(True),
  src = cms.InputTag("generator"),
  abortOnUnknownPDGCode = cms.untracked.bool(False),
)

process.genSelectorFourLep = cms.EDFilter("GenParticleSelector",
  filter = cms.bool(True),
  src = cms.InputTag('genParticlesForFilter'),
  cut = cms.string('(abs(pdgId()) == 11 || abs(pdgId()) == 13 || abs(pdgId()) == 15) && (mother().pdgId() == 23 || abs(mother().pdgId()) == 24)'),
)

process.selectedFourLepCandFilter = cms.EDFilter("CandViewCountFilter",
   src = cms.InputTag('genSelectorFourLep'),
   filter = cms.bool(True),
   minNumber = cms.uint32(4),
)

process.dummy = cms.EDAnalyzer("Dummy")

process.ProductionFilterSequence = cms.Sequence(process.genParticlesForFilter + process.genSelectorFourLep + process.selectedFourLepCandFilter)

process.p = cms.Path(process.ProductionFilterSequence * process.dummy)
process.schedule = cms.Schedule(process.p)
