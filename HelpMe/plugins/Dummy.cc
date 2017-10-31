#include <iostream>
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"

class Dummy : public edm::EDAnalyzer {
   public:
      explicit Dummy(const edm::ParameterSet&);
      ~Dummy();

   private:
      int counter;
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
};

Dummy::Dummy(const edm::ParameterSet& iConfig) : counter(0) {}

Dummy::~Dummy() {}

void Dummy::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  counter++;
}

void Dummy::endJob()
{
  std::cout << "Processed " << counter << " events" << std::endl;
}

void Dummy::beginJob() {}
