<script lang="ts">
	import { goto } from '$app/navigation';
	import Saos from 'saos';
	import RedirectButton from '../components/RedirectButton.svelte';
	import Header from '../components/Header.svelte';
	import Icon from '../components/Icon.svelte';
	import InformationTile from '../components/InformationTile.svelte';
	import AnimationContainer from '../components/AnimationContainer.svelte';
	import Footer from '../components/Footer.svelte';

	let name: string = 'Test';
	let show: boolean = false;

	function onClick() {
		show = !show;
	}

	function navHelp() {
		goto('/help');
	}

	const VIKUS_VIEWER_URL = 'http://localhost:8080/vikus_viewer';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
    class="headline text-center text-base  sm:text- md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none"
	>
		Entdecke die Evolution <br /> von künstlicher Intelligenz
	</h1>
	<h2 class="mt-2 mb-20 text-center text-sm  sm:text-base md:text-lg lg:text-xl xl:text-2xl xl:text-3xl 2xl:text-3xl font-semibold text-gray-400 uppercase">
		Wir nehmen dich mit auf eine Reise durch die Geschichte
	</h2>
	<div class="arrow">
		<Icon
			icon="chevron-down"
			fill_color="none"
			color="#111827CC"
			size="192px"
			class="hover:cursor-pointer hover:scale-105 transition-all duration-500 hover:translate-y-4"
			onClick={() => {goto('#page-content')}}
		/>
	</div>
</div>

<div class="wave-1">
	<svg
		data-name="Layer 1"
		xmlns="http://www.w3.org/2000/svg"
		viewBox="0 0 1200 120"
		preserveAspectRatio="none"
	>
		<path
			d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
			opacity=".25"
			class="shape-fill"
		/>
		<path
			d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
			opacity=".5"
			class="shape-fill"
		/>
		<path
			d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
			class="shape-fill"
		/>
	</svg>
</div>

<div class="background-lightning" />

<div id="page-content" class="section xl:p-12">
	<InformationTile
		title="Vikus Viewer"
		content="Erlebe histrorische Daten auf einem Blick. Erkenne Verläufe, beobachte Trends und untersuche Änderungen."
		class="mt-10 lg:mt-20"
	>
		<div slot="left_slot" class="mt-2 ml-4 flex justify-center  gap-5">
			<Icon icon="bar-chart-2" size="32px" />
			<Icon icon="trending-up" size="32px" />
			<Icon icon="search" size="32px" />
		</div>
		<div slot="right_slot">
			<AnimationContainer from_right>
				<img src="../static/vikusViewer.png" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
			</AnimationContainer>
		</div>
	</InformationTile>
	<InformationTile title="Zusammenhänge schaffen" right_side class="mt-10 lg:mt-20">
		<div slot="content" class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-center lg:text-justify">
			Daten ohne Kontext bringen meist keinen Nutzen. Dadurch haben wir es uns zur Aufgabe gemacht
			einen Zusammenhang zwischen den großen Datenmengen zu schaffen. <br /> Durch NLP
			<span class="font-mono text-xl">(Natural Language Processing)</span> analysieren wir verschiedenste
			Trends in der Geschichte.
		</div>
		<div slot="left_slot" class="mt-2 ml-4 flex flex-row-reverse justify-center gap-5">
			<Icon icon="list" size="32px" />
			<Icon icon="layers" size="32px" />
			<Icon icon="database" size="32px" />
		</div>
		<div slot="right_slot">
			<AnimationContainer>
				<img src="../static/NLP.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
			</AnimationContainer>
		</div>
	</InformationTile>

	<section class="my-32 p-12 text-gray-800 text-center w-[95%] bg-gray-800 rounded-xl">
		<h2 class="text-center text-base  md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl uppercase text-gray-100 font-bold mb-12 pb-4 text-center">
			Neueste Artikel
		</h2>

		<div class="grid lg:grid-cols-3 gap-6 xl:gap-x-12">
			<div class="mb-6 h-full lg:mb-0">
				<div class="relative block bg-white rounded-lg shadow-lg">
					<div class="flex justify-center">
						<div
							class="relative group overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
						>
							<img
								src="../../static/homeml.jpg"
								class="h-72"
								alt="ML"
							/>
							<a href="/tutorial/ml">
								<div
									class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
									style="background-color: rgba(251, 251, 251, 0.15)"
								/>
							</a>
              <a href="https://cdn.futura-sciences.com/buildsv6/images/wide1920/9/0/b/90b0048886_50162050_machine-learning1.jpg" target="_blank" class="opacity-0 bottom-0 left-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 ">
                Quelle: Futura Science
              </a>
						</div>
					</div>
					<div class="flex flex-col justify-center p-2 md:p-6">
						<h5 class="font-bold text-2xl mb-3">Machine Learning</h5>
						<p class="text-gray-500 mb-4">
							<small
								>Veröffentlicht am <u>01.06.2022</u> von
								<p class="text-gray-900">Hamid Omar</p></small
							>
						</p>
						<p class="mb-4 pb-2 text-lg w-[75%] place-self-center">
							Erfahre mehr rund um das Thema Machine Learning und wie es mit Künstlichen
							Intelligenzen zusammenhängt.
						</p>
						<a
							href="/tutorial/ml"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
							class="inline-block px-6 py-2.5 w-auto place-self-center bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
							>Read more</a
						>
					</div>
				</div>
			</div>

			<div class="mb-6 lg:mb-0">
				<div class="relative block bg-white rounded-lg shadow-lg">
					<div class="flex justify-center">
						<div
							class="relative group overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
						>
              <img
                src="../../static/homeki.jpg"
                class="h-96"
                alt="KI"
              />
							<a href="/tutorial/ki">
								<div
									class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
									style="background-color: rgba(251, 251, 251, 0.15)"
								/>
							</a>
              <a href="https://www.planet-wissen.de/sendungen/kuenstliche-intelligenz-roboter-104~_v-gseagaleriexl.jpg" target="_blank" class="opacity-0 bottom-0 left-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 ">
                Quelle: Planet Wissen
              </a>
						</div>
					</div>
					<div class="flex flex-col justify-center p-2 md:p-6">
						<h5 class="font-bold text-2xl mb-3">Künstliche Intelligenz</h5>
						<p class="text-gray-500 mb-4">
							<small
								>veröffentlicht am <u>24.05.2022</u> von
								<p class="text-gray-900">Robert Witzke</p></small
							>
						</p>
						<p class="mb-4 pb-2 text-lg w-[75%] place-self-center">
							Erfahre mehr rund um das Thema Künstliche Intelligenz - von der Begriffsklärung über
							die Historie bis hin zu aktuellen Themen wie Deep Learning.
						</p>
						<a
							href="/tutorial/ki"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
							class="inline-block px-6 py-2.5 w-auto place-self-center bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
							>Read more</a
						>
					</div>
				</div>
			</div>

			<div class="mb-6 lg:mb-0">
				<div class="relative block bg-white rounded-lg shadow-lg">
					<div class="flex justify-center">
						<div
							class="relative group overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
						>
							<img
								src="../../static/homenlp.jpeg"
								class="h-72"
								alt="NLP"
							/>
							<a href="/tutorial/nlp">
								<div
									class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
									style="background-color: rgba(251, 251, 251, 0.15)"
								/>
							</a>
              <a href="https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters:format(jpg)/https:%2F%2Fblogs-images.forbes.com%2Fbernardmarr%2Ffiles%2F2019%2F06%2F5-Amazing-Examples-Of-Natural-Language-Processing-NLP-In-Practice-1200x639.jpeg" target="_blank" class="opacity-0 bottom-0 left-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 ">
                Quelle: Forbes
              </a>
						</div>
					</div>
					<div class="flex flex-col justify-center p-2 md:p-6">
						<h5 class="font-bold text-2xl mb-3">Natural Language Processing</h5>
						<p class="text-gray-500 mb-4">
							<small
								>Veröffentlicht am <u>21.06.2022</u> von
								<p class="text-gray-900">Marten Kaffler</p>
							</small>
						</p>
						<p class="mb-4 pb-2 text-lg w-[75%] place-self-center">
							Erfahre mehr rund um das Thema Natural Language Processing und wie Computer unsere
							natürliche Sprache verstehen und verarbeiten können.
						</p>
						<a
							href="/tutorial/nlp"
							data-mdb-ripple="true"
							data-mdb-ripple-color="light"
							class="inline-block px-6 py-2.5 w-auto place-self-center bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
							>Read more</a
						>
					</div>
				</div>
			</div>
		</div>
	</section>

	<div class="flex flex-col gap-5">
		<RedirectButton text="Zum Tutorial" href="/tutorial" />
		<RedirectButton text="Zum Vikus Viewer" href={VIKUS_VIEWER_URL} />
		<RedirectButton text="Zum NLP-Playground" href="/nlp" />
	</div>

	<Footer />
</div>

<style lang="postcss">
	.background-lightning {
		@apply absolute top-full w-full shadow-white shadow-2xl z-50;
		box-shadow: 0px 0px 180px 10px #fff;
	}

	.arrow {
		@apply bg-transparent;
	}
	.wave-1 {
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		overflow: hidden;
		line-height: 0;
		transform: rotate(180deg);
	}

	.wave-1 svg {
		position: relative;
		display: block;
		width: calc(100% + 1.3px);
		height: 150px;
	}

	.wave-1 .shape-fill {
		fill: #111827;
	}

	.section {
		@apply absolute top-full w-full flex flex-col gap-y-60 items-center bg-gray-900;
	}

	@keyframes -global-from-left {
		0% {
			transform: translateX(-10vw);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
</style>
